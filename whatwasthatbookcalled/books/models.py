from django.db import models


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
    language = models.CharField(max_length=50, blank=True)
    year_written = models.IntegerField(blank=True, null=True)
    year_read = models.PositiveIntegerField(blank=True, null=True)
    part_of_series = models.BooleanField(null=True, choices=PART_OF_SERIES_CHOICES)
    cover_description = models.TextField(blank=True)
    genre = models.ManyToManyField(blank=True, to=BookGenre)
    plot_details = models.TextField(blank=True)
    quotes = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
