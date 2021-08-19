from django.db.models.deletion import CASCADE
from whatwasthatbookcalled.books_auth.models import BookUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from languages import languages


class BookGenre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    PART_OF_SERIES_CHOICES = (
        (None, "Can't remember"),
        (True, "Yes"),
        (False, "No"),
    )

    title_tips = models.TextField(blank=True)
    author_tips = models.TextField(blank=True)
    language = models.CharField(max_length=50, blank=True, choices=languages)
    year_written = models.IntegerField(blank=True, null=True)
    year_read = models.PositiveIntegerField()
    part_of_series = models.BooleanField(
        null=True, blank=True, choices=PART_OF_SERIES_CHOICES
    )
    cover_description = models.TextField(blank=True)
    genre = models.ManyToManyField(blank=True, to=BookGenre)
    plot_details = models.TextField(blank=True)
    quotes = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    solved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    filled_fields_count = models.PositiveIntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(11)]
    )
    user = models.ForeignKey(to=BookUser, on_delete=CASCADE)

    @property
    def main_field(self):
        if self.plot_details:
            return "plot"
        elif self.quotes:
            return "quotes"
        elif self.cover_description:
            return "cover description"

    @property
    def comment_count(self):
        return self.comment_set.all().count()

    @property
    def comments_by_last_modified(self):
        return self.comment_set.all().order_by("-last_modified")

    @property
    def short_fields(self):
        return {
            "Title tips": self.title_tips,
            "Author tips": self.author_tips,
            "Language": self.language,
            "Year read": self.year_read,
            "Year written": self.year_written,
        }

    @property
    def long_fields(self):
        return {
            "Genre": self.genre,
            "Cover description": self.cover_description,
            "Plot details": self.plot_details,
            "Quotes": self.quotes,
            "Additional notes": self.additional_notes,
        }

    @property
    def book_genres_as_list(self):
        book_genres = list(self.genre.all().values())
        book_genres_ids = [x["id"] for x in book_genres]
        return book_genres_ids


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(to=BookUser, on_delete=CASCADE)
    book = models.ForeignKey(to=Book, on_delete=CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    is_solution = models.BooleanField(default=False)
