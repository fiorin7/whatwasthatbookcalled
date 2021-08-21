from django.core.exceptions import ObjectDoesNotExist
from whatwasthatbookcalled.books.models import Book, Comment
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class AllBooksTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client()
        cls.response = client.get(reverse("all books"))

    def test_UsesTemplate(self):
        response = AllBooksTest.response
        self.assertTemplateUsed(response, "books/all-books.html")

    def test_HasLanguagesInContext(self):
        response = AllBooksTest.response
        self.assertIn("languages", response.context)

    def test_UsesForm(self):
        response = AllBooksTest.response
        self.assertIn("filter_sort_form", response.context)

    def test_BooksAreOrdered(self):
        response = AllBooksTest.response
        self.assertTrue(response.context["books"].object_list.ordered)

    def test_BooksArePaginated(self):
        response = AllBooksTest.response
        self.assertTrue(hasattr(response.context["books"], "paginator"))


class CreateTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        cls.client = Client()

    def test_UsesTemplate(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.get(reverse("create"))
        self.assertTemplateUsed(response, "books/create.html")

    def test_UsesForm(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.get(reverse("create"))
        self.assertIn("form", response.context)

    def test_NeedsLogin(self):
        response = CreateTest.client.get(reverse("create"))
        self.assertTemplateNotUsed(response, "books/create.html")

    def test_ManyToManySaved(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.post(
            reverse("create"),
            {
                "title_tips": [""],
                "author_tips": [""],
                "language": [""],
                "year_written": [""],
                "year_read": ["2000"],
                "part_of_series": [""],
                "cover_description": [""],
                "genre": ["2", "3"],
                "plot_details": ["lorem"],
                "quotes": [""],
                "additional_notes": [""],
            },
        )
        book = Book.objects.get(plot_details="lorem")
        self.assertListEqual([2, 3], book.book_genres_as_list)


class DetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        cls.book1 = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=3,
            user=cls.user,
            language="Arabic",
        )
        cls.book1.full_clean()
        cls.book1.save()
        cls.client = Client()

        cls.response_get = cls.client.get(
            reverse("details", kwargs={"id": cls.book1.id})
        )
        cls.response_post = cls.client.post(
            reverse("details", kwargs={"id": cls.book1.id})
        )

    def test_UsesTemplate(self):
        response = DetailsTest.response_get
        self.assertTemplateUsed(response, "books/details.html")

    def test_WhenUnauthenticatedTriesToPost_Redirects(self):
        response = DetailsTest.response_post
        self.assertRedirects(response, f"/auth/sign-in/")

    def test_MarkCommentAsSolution(self):
        DetailsTest.client.login(username="diana", password="diana")

        comment = Comment(text="Lorem", user=DetailsTest.user, book=DetailsTest.book1)
        comment.save()
        response = DetailsTest.client.get(
            reverse(
                "solution pick",
                kwargs={"book_id": DetailsTest.book1.id, "comment_id": comment.id},
            )
        )
        self.assertTrue(Book.objects.get(id=DetailsTest.book1.id).solved)
        self.assertTrue(Comment.objects.get(id=comment.id).is_solution)


class EditBookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        cls.book1 = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=3,
            user=cls.user,
            language="Arabic",
        )
        cls.book1.full_clean()
        cls.book1.save()
        cls.client = Client()

    def test_UsesTemplate(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.get(
            reverse("edit", kwargs={"book_id": EditBookTest.book1.id})
        )
        self.assertTemplateUsed(response, "books/edit-book.html")

    def test_UsesForm(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.get(
            reverse("edit", kwargs={"book_id": EditBookTest.book1.id})
        )
        self.assertIn("form", response.context)

    def test_NeedsLogin(self):
        response = CreateTest.client.get(
            reverse("edit", kwargs={"book_id": EditBookTest.book1.id})
        )
        self.assertTemplateNotUsed(response, "books/edit-book.html")

    def test_ManyToManySaved(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.post(
            reverse("edit", kwargs={"book_id": EditBookTest.book1.id}),
            {
                "title_tips": [""],
                "author_tips": [""],
                "language": [""],
                "year_written": [""],
                "year_read": ["2000"],
                "part_of_series": [""],
                "cover_description": [""],
                "genre": ["2", "3"],
                "plot_details": ["lorem"],
                "quotes": [""],
                "additional_notes": [""],
            },
        )
        book = Book.objects.get(plot_details="lorem")
        self.assertListEqual([2, 3], book.book_genres_as_list)


class DeleteBookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        cls.book1 = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=3,
            user=cls.user,
            language="Arabic",
        )
        cls.book1.full_clean()
        cls.book1.save()
        cls.client = Client()

    def test_NeedsAuthorisation(self):
        response = CreateTest.client.get(
            reverse("delete", kwargs={"book_id": DeleteBookTest.book1.id})
        )
        self.assertRedirects(
            response,
            f"/auth/sign-in?next=/books/{DeleteBookTest.book1.id}/delete",
            fetch_redirect_response=False,
        )

    def test_BookDeleted(self):
        CreateTest.client.login(username="diana", password="diana")
        response = CreateTest.client.get(
            reverse("delete", kwargs={"book_id": DeleteBookTest.book1.id})
        )
        with self.assertRaises(ObjectDoesNotExist):
            Book.objects.get(id=DeleteBookTest.book1.id)
