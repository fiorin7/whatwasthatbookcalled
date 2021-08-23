from whatwasthatbookcalled.profiles.models import Profile
from whatwasthatbookcalled.books.models import Book, BookGenre
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
import tempfile


class ProfileTest(TestCase):
    def test_WhenProfilePicture_ReturnProfilePuctureUrl(self):
        user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        file = tempfile.NamedTemporaryFile(suffix=".png")
        image = ImageFile(file, name=file.name)
        p = Profile(profile_picture=image, user=user)
        self.assertNotEqual(
            p.profile_picture_url, "/static/images/default_profile_picture.png"
        )

    def test_WhenNoProfilePicture_ReturnDefaultProfilePuctureUrl(self):
        user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        p = Profile(user=user)
        self.assertEqual(
            p.profile_picture_url, "/static/images/default_profile_picture.png"
        )
