from django.db import models
import whatwasthatbookcalled.profiles.services as ProfileService
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BookUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), blank=False, unique=True)

    def __str__(self):
        return self.username

    @property
    def profile(self):
        return ProfileService.get_by_id(self.id)

    @property
    def date_joined_string(self):
        return self.date_joined.strftime("%b %d, %Y")

    @property
    def books(self):
        return self.book_set.all().order_by("-last_modified")

    @property
    def comments(self):
        return self.comment_set.all().order_by("-last_modified")

    @property
    def books_count(self):
        return self.book_set.all().count()

    @property
    def comments_count(self):
        return self.comment_set.all().count()

    @property
    def solutions_count(self):
        return self.comment_set.filter(is_solution=True).count()
