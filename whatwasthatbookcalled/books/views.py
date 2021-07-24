from whatwasthatbookcalled.books.foms import BookForm
from django.shortcuts import render


def create(req):
    if req.method == "GET":
        form = BookForm()
        return render(req, "books/create.html", context={"form": form})
    elif req.method == "POST":
        form = BookForm(req.POST)
        if form.is_valid():
            print(req.POST)
            form.save()
        else:
            print(req.POST)

            return render(req, "books/create.html", context={"form": form})
