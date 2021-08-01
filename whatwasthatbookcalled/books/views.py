from django.shortcuts import redirect, render
from django.db.models import QuerySet

from whatwasthatbookcalled.books.models import Book
from whatwasthatbookcalled.books.foms import BookForm, FilterForm, SortForm
from languages import languages


def index(req):
    filter_form = FilterForm(req.GET)
    sort_form = SortForm(req.GET)
    context = {"languages": languages}
    books = Book.objects.all()

    language = req.GET.get("language")
    genre = req.GET.get("genre")
    solved = req.GET.get("solved")

    sort_by = req.GET.get("sort_by")
    descending = req.GET.get("descending")

    if language:
        books = books.filter(language=language)
    if genre:
        books = books.filter(genre=genre)
    if solved:
        books = books.filter(solved=solved)

    context["books"] = books
    context["filter_form"] = filter_form
    context["sort_form"] = sort_form

    return render(req, "books/index.html", context=context)


def create(req):
    if req.method == "GET":
        form = BookForm()
        return render(req, "books/create.html", context={"form": form})
    elif req.method == "POST":
        form = BookForm(req.POST)
        if form.is_valid():
            book = form.save(commit=False)

            filled_fields = [
                x
                for x in form.cleaned_data.values()
                if x != ""
                and x is not None
                and not (isinstance(x, QuerySet) and len(x) == 0)
            ]
            book.filled_fields_count = len(filled_fields)
            book.save()

            return redirect("index")
        else:
            print(req.POST)
            print("INVALID")
            return render(req, "books/create.html", context={"form": form})
