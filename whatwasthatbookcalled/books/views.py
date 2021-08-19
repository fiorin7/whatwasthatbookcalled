import whatwasthatbookcalled.books.services as BookService
import whatwasthatbookcalled.profiles.services as ProfileService
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.db.models import QuerySet

from whatwasthatbookcalled.books.models import Comment
from whatwasthatbookcalled.books.foms import BookForm, CommentForm, FilterSortForm
from whatwasthatbookcalled.profiles.models import Profile
from languages import languages

fields_per_page = {
    "__all__": 1,
    "title_tips": 1,
    "author_tips": 1,
    "language": 1,
    "year_written": 2,
    "year_read": 2,
    "part_of_serie": 2,
    "cover_description": 2,
    "genre": 3,
    "plot_details": 3,
    "quotes": 3,
    "additional_notes": 3,
}


def index(req):
    filter_sort_form = FilterSortForm(req.GET)
    context = {"languages": languages}
    filtered_books = BookService.filter_all_by_GET_params(req.GET)
    sorted_books = BookService.sort_filtered_by_GET_params(req.GET, filtered_books)

    for book in sorted_books:
        book.comment_count = book.comment_set.all().count()

    context["books"] = sorted_books
    context["filter_sort_form"] = filter_sort_form

    return render(req, "books/index.html", context=context)


@login_required
def create(req):
    if req.method == "GET":
        form = BookForm()
        return render(
            req, "books/create.html", context={"form": form, "first_error_page": None}
        )
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
            for field in form.errors.keys():
                first_error_page = fields_per_page[field]
            print("INVALID")
            return render(
                req,
                "books/create.html",
                context={"form": form, "first_error_page": first_error_page},
            )


def details(req, id):
    profile = None
    if req.user.is_authenticated:
        profile = ProfileService.get_by_id(req.user.id)

    book = BookService.get_by_id(id)

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
        comment.user_photo = ProfileService.get_by_id(
            comment.user.id
        ).profile_picture_url

    context = {
        "book_short_fields": book_short_fields,
        "book_long_fields": books_long_fields,
        "comments": comments,
        "book_user": book.user,
        "book_id": book.id,
        "book_user_id": book.user.id,
        "book_solved": book.solved,
        "book_user_photo": ProfileService.get_by_id(book.user.id).profile_picture_url,
        "current_user_photo": profile.profile_picture_url if profile else None,
    }

    if req.method == "GET":
        comment_form = CommentForm()
        context["comment_form"] = comment_form

        return render(req, "books/details.html", context)

    if not req.user.is_authenticated:
        return redirect("sign in")
    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = req.user
        comment.book = book
        comment.save()
        return redirect("details", id)

    else:
        context["comment_form"] = comment_form

        return render(req, "books/details.html", context)


@login_required
def mark_comment_as_solution(req, book_id, comment_id):
    book = BookService.get_by_id(book_id)
    comment = Comment.objects.get(id=comment_id)

    if not book.solved and req.user == book.user:
        book.solved = True
        book.save()

        comment.is_solution = True
        comment.save()

        return redirect("details", book_id)
    else:
        return redirect("details", book.id)


@login_required
def edit_book(req, book_id):
    book = BookService.get_by_id(id=book_id)
    book_genres = list(book.genre.all().values())
    book_genres_ids = [x["id"] for x in book_genres]

    if book.user != req.user:
        return redirect("details", book_id)

    if req.method == "GET":
        form = BookForm(instance=book)

        return render(
            req,
            "books/edit-book.html",
            {
                "form": form,
                "book_id": book.id,
                "book_user": book.user,
                "book_user_photo": ProfileService.get_by_id(
                    book.user.id
                ).profile_picture_url,
                "book_genres_ids": book_genres_ids,
            },
        )

    form = BookForm(req.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect("details", book_id)
    else:
        return render(
            req,
            "books/edit-book.html",
            {
                "form": form,
                "book_id": book.id,
                "book_user": book.user,
                "book_user_photo": ProfileService.get_by_id(
                    book.user.id
                ).profile_picture_url,
                "book_genres_ids": book_genres_ids,
            },
        )
