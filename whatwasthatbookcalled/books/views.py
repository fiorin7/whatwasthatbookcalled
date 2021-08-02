from datetime import datetime, timezone

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
        "last_modified",
    )

    sort_by = req.GET.get("sort_by")
    reverse_order = req.GET.get("reverse_order")
    order_prefix = "" if reverse_order else "-"

    if sort_by is None or sort_by == "date":
        books = books.order_by(order_prefix + "last_modified")
    elif sort_by == "info-amount":
        books = books.order_by(order_prefix + "filled_fields_count")

    for book in books:
        timedelta = datetime.now(timezone.utc) - book.last_modified
        days = timedelta.days
        hours = timedelta.total_seconds() // 3600
        minutes = timedelta.total_seconds() // 60

        book_time = "just now"
        book_time_unit = None

        if days > 0:
            book_time = days
            book_time_unit = "days"
        elif hours > 0:
            book_time = int(hours)
            book_time_unit = "hours"
        elif minutes > 0:
            book_time = int(minutes)
            book_time_unit = "minutes"

        book.time = book_time
        book.time_unit = book_time_unit

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
