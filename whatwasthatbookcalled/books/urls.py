from django.urls.conf import path
from whatwasthatbookcalled.books.views import (
    create,
    delete_book,
    details,
    edit_book,
    index,
    mark_comment_as_solution,
)


urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("details/<int:id>", details, name="details"),
    path(
        "solution-pick/<int:book_id>/<int:comment_id>",
        mark_comment_as_solution,
        name="solution pick",
    ),
    path("<int:book_id>/delete", delete_book, name="delete"),
]
