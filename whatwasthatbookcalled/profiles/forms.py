from django import forms
from whatwasthatbookcalled.profiles.models import Profile


class ProfileEditBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio",)

        labels = {"bio": ""}
        widgets = {
            "bio": forms.Textarea(
                attrs={"cols": 25, "rows": 5, "onblur": "this.form.submit();"}
            )
        }


class ProfileEditProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_picture",)

        labels = {"profile_picture": ""}
        widgets = {
            "profile_picture": forms.FileInput(
                attrs={"onchange": "this.form.submit();"}
            )
        }
