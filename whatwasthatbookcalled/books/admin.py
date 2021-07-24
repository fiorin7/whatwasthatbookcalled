from django.contrib import admin
from whatwasthatbookcalled.books.models import Book, BookGenre

# Register your models here.

admin.site.register(Book)

admin.site.register(BookGenre)
