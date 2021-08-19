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
