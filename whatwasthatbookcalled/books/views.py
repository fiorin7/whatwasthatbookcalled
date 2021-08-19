from whatwasthatbookcalled.books.utils import get_first_error_page
import whatwasthatbookcalled.books.services as BookService
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from whatwasthatbookcalled.books.models import Comment
from whatwasthatbookcalled.books.foms import BookForm, CommentForm, FilterSortForm
from languages import languages


def index(req):
    filter_sort_form = FilterSortForm(req.GET)
    context = {"languages": languages}
    filtered_books = BookService.filter_all_by_GET_params(req.GET)
    sorted_books = BookService.sort_filtered_by_GET_params(req.GET, filtered_books)

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

    form = BookForm(req.POST)
    if form.is_valid():
        book = BookService.get_book_with_user_and_filled_fields(form, req.user)
        book.save()
        form.save_m2m()
        return redirect("index")

    else:
        first_error_page = get_first_error_page(form.errors)

        return render(
            req,
            "books/create.html",
            context={"form": form, "first_error_page": first_error_page},
        )


def details(req, id):
    book = BookService.get_by_id(id)

    context = {
        "book": book,
        "current_user_photo": req.user.profile.profile_picture_url
        if req.user.is_authenticated
        else None,
    }

    if req.method == "GET":
        comment_form = CommentForm()
        context["comment_form"] = comment_form

        return render(req, "books/details.html", context)

    if not req.user.is_authenticated:
        return redirect("sign in")

    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        comment = BookService.get_comment_with_user_and_book(
            comment_form, req.user, book
        )
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
    book_genres_ids = book.book_genres_as_list

    if book.user != req.user:
        return redirect("details", book_id)

    context = {
        "book_id": book.id,
        "book_user": book.user,
        "book_user_photo": book.user.profile.profile_picture_url,
        "book_genres_ids": book_genres_ids,
    }

    if req.method == "GET":
        context["form"] = BookForm(instance=book)

        return render(req, "books/edit-book.html", context)

    form = BookForm(req.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect("details", book_id)
    else:
        context["form"] = form
        return render(req, "books/edit-book.html", context)
