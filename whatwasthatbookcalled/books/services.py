from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from whatwasthatbookcalled.books.models import Book


def get_by_id(id):
    return Book.objects.get(id=id)


def get_all():
    return Book.objects.all()


def filter_all_by_GET_params(get_req):
    filter_params = ["language", "genre", "solved"]
    filters = {}
    for f in filter_params:
        value = get_req.get(f)
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
        "filled_fields_count",
    )

    return books


def sort_filtered_by_GET_params(get_req, filtered_books):
    sort_by = get_req.get("sort_by")
    reverse_order = get_req.get("reverse_order")
    order_prefix = "" if reverse_order else "-"

    if sort_by is None or sort_by == "date":
        books = filtered_books.order_by(order_prefix + "last_modified")
    elif sort_by == "info-amount":
        books = filtered_books.order_by(order_prefix + "filled_fields_count")
    elif sort_by == "popularity":
        books = filtered_books.annotate(comment_count_sort=Count("comment")).order_by(
            order_prefix + "comment_count_sort"
        )

    return books


def get_book_with_user_and_filled_fields(form, user):
    book = form.save(commit=False)

    book.user = user

    filled_fields = [
        x
        for x in form.cleaned_data.values()
        if x != "" and x is not None and not (isinstance(x, QuerySet) and len(x) == 0)
    ]
    book.filled_fields_count = len(filled_fields)

    return book


def get_comment_with_user_and_book(form, user, book):
    comment = form.save(commit=False)
    comment.user = user
    comment.book = book
    return comment
