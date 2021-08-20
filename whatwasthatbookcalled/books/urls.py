from django.urls.conf import path
from whatwasthatbookcalled.books.views import (
    create,
    delete_book,
    delete_comment,
    details,
    edit_book,
    edit_comment,
    all_books,
    mark_comment_as_solution,
)


urlpatterns = [
    path("", all_books, name="all books"),
    path("create/", create, name="create"),
    path("<int:id>/details", details, name="details"),
    path(
        "solution-pick/<int:book_id>/<int:comment_id>",
        mark_comment_as_solution,
        name="solution pick",
    ),
    path("<int:book_id>/edit", edit_book, name="edit"),
    path("<int:book_id>/delete", delete_book, name="delete"),
    path(
        "<int:book_id>/edit-comment/<int:comment_id>", edit_comment, name="edit comment"
    ),
    path(
        "<int:book_id>/delete-comment/<int:comment_id>",
        delete_comment,
        name="delete comment",
    ),
]
