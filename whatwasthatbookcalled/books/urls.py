from django.urls.conf import path
from whatwasthatbookcalled.books.views import create


urlpatterns = [
    path("create/", create, name="create"),
]
