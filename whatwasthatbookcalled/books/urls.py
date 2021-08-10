from django.urls.conf import path
from whatwasthatbookcalled.books.views import create, details, index


urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("details/<int:id>", details, name="details"),
]
