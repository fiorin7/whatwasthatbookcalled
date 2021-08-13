from django.db import models
from django.db.models.deletion import CASCADE
from whatwasthatbookcalled.books_auth.models import BookUser


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to="profile_pictures")
    bio = models.TextField()
    user = models.OneToOneField(to=BookUser, on_delete=CASCADE, primary_key=True)
