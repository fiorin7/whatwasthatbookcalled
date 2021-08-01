from django.urls.conf import path
from whatwasthatbookcalled.books.views import create, index


urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
]
