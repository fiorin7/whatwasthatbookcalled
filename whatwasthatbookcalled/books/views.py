from whatwasthatbookcalled.books.foms import BookForm
from django.shortcuts import render


def create(req):
    form = BookForm()
    return render(req, "books/create.html", context={"form": form})
