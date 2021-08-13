from datetime import datetime, timezone

from django.shortcuts import redirect, render
from django.db.models import QuerySet

from whatwasthatbookcalled.books.models import Book, Comment
from whatwasthatbookcalled.books.foms import BookForm, CommentForm, FilterSortForm
from whatwasthatbookcalled.profiles.models import Profile
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

        book.comment_count = book.comment_set.all().count()

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

            book.user = req.user

            filled_fields = [
                x
                for x in form.cleaned_data.values()
                if x != ""
                and x is not None
                and not (isinstance(x, QuerySet) and len(x) == 0)
            ]
            book.filled_fields_count = len(filled_fields)
            book.save()
            form.save_m2m()

            return redirect("index")
        else:
            print(req.POST)
            print("INVALID")
            return render(req, "books/create.html", context={"form": form})


def details(req, id):
    profile = Profile.objects.get(user_id=req.user.id)
    current_user = req.user

    book = Book.objects.get(id=id)

    book_short_fields = {
        "Title tips": book.title_tips,
        "Author tips": book.author_tips,
        "Language": book.language,
        "Year read": book.year_read,
        "Year written": book.year_written,
    }

    books_long_fields = {
        "Genre": book.genre,
        "Cover description": book.cover_description,
        "Plot details": book.plot_details,
        "Quotes": book.quotes,
        "Additional notes": book.additional_notes,
    }

    comments = book.comment_set.all().order_by("-last_modified")
    for comment in comments:
        comment.user_photo = Profile.objects.get(
            user_id=comment.user.id
        ).profile_picture

    if req.method == "GET":
        comment_form = CommentForm()

        return render(
            req,
            "books/details.html",
            context={
                "book_short_fields": book_short_fields,
                "book_long_fields": books_long_fields,
                "comment_form": comment_form,
                "comments": comments,
                "book_user": book.user,
                "book_id": book.id,
                "book_user_id": book.user.id,
                "book_solved": book.solved,
                "book_user_photo": Profile.objects.get(
                    user_id=book.user.id
                ).profile_picture,
                "current_user_photo": profile.profile_picture,
                "current_user_id": current_user.id,
            },
        )

    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = req.user
        comment.book = book
        comment.save()
        return redirect("details", id)

    else:
        return render(
            req,
            "books/details.html",
            context={
                "book_short_fields": book_short_fields,
                "book_long_fields": books_long_fields,
                "comment_form": comment_form,
                "comments": comments,
                "book_user": book.user,
                "book_id": book.id,
                "book_solved": book.solved,
                "book_user_id": book.user.id,
                "book_user_photo": Profile.objects.get(
                    user_id=book.user.id
                ).profile_picture,
                "current_user_photo": profile.profile_picture,
                "current_user_id": current_user.id,
            },
        )


def mark_comment_as_solution(req, book_id, comment_id):
    book = Book.objects.get(id=book_id)
    comment = Comment.objects.get(id=comment_id)

    if not book.solved and req.user == book.user:
        book.solved = True
        book.save()

        comment.is_solution = True
        comment.save()

        return redirect("details", book_id)
    else:
        return redirect("details", book.id)
