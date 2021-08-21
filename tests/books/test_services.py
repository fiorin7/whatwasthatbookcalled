from datetime import datetime
from unittest import mock
from whatwasthatbookcalled.books.services import (
    filter_all_by_GET_params,
    get_book_with_user_and_filled_fields,
    get_comment_with_user_and_book,
    sort_filtered_by_GET_params,
)
from whatwasthatbookcalled.books.models import Book, BookGenre, Comment
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase, Client
from unittest.mock import patch


class BookServicesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = BookUser(email="diana@abv.bg", username="diana", password="diana")
        cls.user.save()
        cls.book1 = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            author_tips="Lorem ipsum",
            filled_fields_count=3,
            user=cls.user,
            last_modified=datetime(2020, 1, 1, 1, 1),
            language="Arabic",
        )
        cls.book1.full_clean()
        cls.book1.save()
        genre1 = BookGenre.objects.get(id=1)
        cls.book1.genre.add(genre1)
        cls.book1.solved = True
        cls.book1.save()

        cls.book2 = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=2,
            user=cls.user,
            last_modified=datetime(2020, 2, 1, 1, 1),
        )
        cls.book2.full_clean()
        cls.book2.save()
        genre2 = BookGenre.objects.get(id=2)
        cls.book2.genre.add(genre2)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_FilterByLanguage(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"language": "Arabic"}
        result = filter_all_by_GET_params(GET)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, BookServicesTest.book1.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_FilterByGenre(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"genre": 2}
        result = filter_all_by_GET_params(GET)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, BookServicesTest.book2.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_FilterBySolved(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"solved": True}
        result = filter_all_by_GET_params(GET)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, BookServicesTest.book1.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_FilterByLanguageAndGenre(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"language": "Arabic", "genre": 2}
        result = filter_all_by_GET_params(GET)

        self.assertEqual(len(result), 0)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_WhenNoSort_SortByDate(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {}

        result = filter_all_by_GET_params(GET)
        result = sort_filtered_by_GET_params(GET, result)

        self.assertEqual(result[0].id, BookServicesTest.book2.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_SortByDate(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"sort_by": "date"}

        result = filter_all_by_GET_params(GET)
        result = sort_filtered_by_GET_params(GET, result)

        self.assertEqual(result[0].id, BookServicesTest.book2.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_SortByDateReverseOrder(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]
        GET = {"sort_by": "date", "reverse_order": True}

        result = filter_all_by_GET_params(GET)
        result = sort_filtered_by_GET_params(GET, result)

        self.assertEqual(result[0].id, BookServicesTest.book1.id)

    @patch("whatwasthatbookcalled.books.models.Book")
    def test_SortByPopularity(self, patch_post):
        patch_post.objects.return_value = [
            BookServicesTest.book1,
            BookServicesTest.book2,
        ]

        comment1 = Comment(
            text="Lorem ipsum", user=BookServicesTest.user, book=BookServicesTest.book1
        )
        comment1.save()

        GET = {"sort_by": "popularity"}

        result = filter_all_by_GET_params(GET)
        result = sort_filtered_by_GET_params(GET, result)

        self.assertEqual(result[0].id, BookServicesTest.book1.id)

    def test_GetBookWithUserAndFilledFields(self):
        book = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            author_tips="Lorem ipsum",
            last_modified=datetime(2020, 1, 1, 1, 1),
            language="Arabic",
        )
        m = mock.Mock()
        m.save.return_value = book
        m.cleaned_data = {
            "year_read": 1997,
            "plot_details": "Lorem ipsum",
            "author_tips": "Lorem ipsum",
            "language": "Arabic",
        }
        book_modified = get_book_with_user_and_filled_fields(m, BookServicesTest.user)

        self.assertEqual(book_modified.filled_fields_count, 4)
        self.assertEqual(book_modified.user, BookServicesTest.user)

    def test_GetCommentWithUserAndBook(self):
        comment = Comment(text="Lorem ipsum")
        m = mock.Mock()
        m.save.return_value = comment

        comment_modified = get_comment_with_user_and_book(
            m, BookServicesTest.user, BookServicesTest.book1
        )

        self.assertEqual(comment_modified.book, BookServicesTest.book1)
        self.assertEqual(comment_modified.user, BookServicesTest.user)
