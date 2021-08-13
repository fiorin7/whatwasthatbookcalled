from django.contrib.auth import get_user_model
from django import forms
from whatwasthatbookcalled.books_auth.models import BookUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].help_text = None
        self.fields["password1"].label = ""
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )

        self.fields["password2"].help_text = None
        self.fields["password2"].label = ""
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"placeholder": "Password confirmation"}
        )

    class Meta:

        model = BookUser
        fields = ("username", "email")

        help_texts = {"username": None}

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
        }

        labels = {"username": "", "email": "", "password1": "", "password2": ""}


class LoginForm(AuthenticationForm):
    pass
