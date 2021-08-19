from django.db import models
from django.db.models.deletion import CASCADE
from django.templatetags.static import static


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to="profile_pictures")
    bio = models.TextField()
    user = models.OneToOneField(
        to="books_auth.BookUser", on_delete=CASCADE, primary_key=True
    )

    @property
    def profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return static("images/default_profile_picture.jpg")
