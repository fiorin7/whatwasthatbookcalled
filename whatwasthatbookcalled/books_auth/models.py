from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class BookUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), blank=False, unique=True)

    def __str__(self):
        return self.username
