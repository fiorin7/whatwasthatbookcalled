from whatwasthatbookcalled.books.models import Book, BookGenre
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase
from django.core.exceptions import ValidationError


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = BookUser(email="diana@abv.bg", username="diana", password="diana")
        cls.user.save()

    def test_whenOnlyPlot_expectMainFieldPlot(self):
        b = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=2,
            user=BookTest.user,
        )

        b.full_clean()
        b.save()

        self.assertEqual(b.main_field, "plot")

    def test_whenOnlCoverDesv_expectMainFieldCoverDesc(self):
        b = Book(
            year_read=1997,
            cover_description="Lorem ipsum",
            filled_fields_count=2,
            user=BookTest.user,
        )

        b.full_clean()
        b.save()

        self.assertEqual(b.main_field, "cover description")

    def test_whenPlotDetailsAndCoverDesc_expectMainFieldPlot(self):
        b = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            cover_description="Lorem ipsum",
            filled_fields_count=2,
            user=BookTest.user,
        )

        b.full_clean()
        b.save()

        self.assertEqual(b.main_field, "plot")

    def test_BookGenresAsList(self):
        b = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=2,
            user=BookTest.user,
        )

        b.full_clean()
        b.save()

        genre1 = BookGenre.objects.get(id=1)
        genre2 = BookGenre.objects.get(id=2)

        b.genre.add(genre1)
        b.genre.add(genre2)

        self.assertEqual(b.book_genres_as_list, [1, 2])
