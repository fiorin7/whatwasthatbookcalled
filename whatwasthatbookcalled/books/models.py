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
    author_tips = models.TextField()
    language = models.CharField(max_length=50)
    year_written = models.IntegerField()
    year_read = models.PositiveIntegerField()
    part_of_series = models.BooleanField(null=True, choices=PART_OF_SERIES_CHOICES)
    cover_description = models.TextField()
    genre = models.ManyToManyField(to=BookGenre)
    plot_details = models.TextField()
    quotes = models.TextField()
    additional_notes = models.TextField()
