from django.shortcuts import redirect, render
from django.db.models import QuerySet

from whatwasthatbookcalled.books.models import Book
from whatwasthatbookcalled.books.foms import BookForm, FilterSortForm
from languages import languages


def index(req):
    filter_sort_form = FilterSortForm(req.GET)
    context = {"languages": languages}

    filter_params = ["language", "genre", "solved"]

    filters = {}
    for f in filter_params:
        value = req.GET.get(f)
        if value is not None and value != "":
            filters[f] = value

    books = Book.objects.filter(**filters).only(
        "year_read",
        "plot_details",
        "cover_description",
        "quotes",
        "solved",
        "genre",
    )

    sort_by = req.GET.get("sort_by")
    descending = req.GET.get("descending")

    if language:
        books = books.filter(language=language)
    if genre:
        books = books.filter(genre=genre)
    if solved:
        books = books.filter(solved=solved)

    context["books"] = books
    context["filter_sort_form"] = filter_sort_form

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
