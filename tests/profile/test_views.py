from whatwasthatbookcalled.profiles.models import Profile
from whatwasthatbookcalled.books_auth.models import BookUser
from django.test import TestCase, Client
from django.urls import reverse


class ProfileViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = BookUser.objects.create_user(
            email="diana@abv.bg", username="diana", password="diana"
        )
        cls.client = Client()

    def test_LoginRequired(self):
        response = ProfileViewsTest.client.get(reverse("profile"))
        self.assertTemplateNotUsed(response, "profiles/profile.html")

    def test_UsesForm(self):
        ProfileViewsTest.client.login(username="diana", password="diana")
        response = ProfileViewsTest.client.get(reverse("profile"))
        self.assertIn("form", response.context)

    def test_EditBio(self):
        ProfileViewsTest.client.login(username="diana", password="diana")

        p = Profile(user=ProfileViewsTest.user)
        p.save()
        response = ProfileViewsTest.client.post(reverse("edit bio"), {"bio": "My bio"})
        self.assertEqual(
            Profile.objects.get(user_id=ProfileViewsTest.user.id).bio, "My bio"
        )
