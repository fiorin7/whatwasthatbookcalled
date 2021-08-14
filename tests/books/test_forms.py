from whatwasthatbookcalled.books.foms import BookForm
from whatwasthatbookcalled.books.models import Book
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase
from django.core.exceptions import ValidationError


class BookFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = BookUser(email="diana@abv.bg", username="diana", password="diana")
        cls.user.save()
        cls.book = Book(
            year_read=1997,
            plot_details="Lorem ipsum",
            filled_fields_count=2,
            user=BookFormTest.user,
        )

        cls.book.full_clean()
        cls.book.save()
        # cls.form = BookForm()

    def test_whenNoPlotNoQuotesNoCoverDesc_expectInvalid(self):
        form = BookForm({"year_read": 1997})

        self.assertFalse(form.is_valid())

    def test_whenOnlyPlot_expectValid(self):
        form = BookForm({"year_read": 1997, "plot_details": "Lorem ipsum"})

        self.assertTrue(form.is_valid())
