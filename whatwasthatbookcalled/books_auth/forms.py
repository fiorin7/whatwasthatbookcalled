from django.contrib.auth import get_user_model
from whatwasthatbookcalled.books_auth.models import BookUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:

        model = BookUser
        fields = ("username", "email")


class LoginForm(AuthenticationForm):
    pass
