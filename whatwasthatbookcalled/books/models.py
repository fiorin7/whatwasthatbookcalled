from django.db import models


class Book(models.Model):
    title_tips = models.TextField(blank=True)
    author_tips = models.TextField()
    language = models.CharField(max_length=50)
    year_written = models.IntegerField()
    year_read = models.PositiveIntegerField()
    part_of_series = models.CharField(max_length=50)
    cover_description = models.TextField()
    genre = models.CharField(max_length=50)
    plot_details = models.TextField()
    quotes = models.TextField()
    additional_notes = models.TextField()
