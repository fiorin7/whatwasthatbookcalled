from django.urls import path
from whatwasthatbookcalled.profiles.views import (
    profile,
    profile_edit_bio,
    profile_show_all_books,
    profile_show_all_comments,
)
import whatwasthatbookcalled.profiles.signals


urlpatterns = [
    path("", profile, name="profile"),
    path("edit-bio", profile_edit_bio, name="edit bio"),
    path("show-all-books", profile_show_all_books, name="show all books"),
    path("show-all-comments", profile_show_all_comments, name="show all comments"),
]
