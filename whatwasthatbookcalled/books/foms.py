from django import forms
from django.db.models import QuerySet
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["solved", "filled_fields_count"]

        widgets = {
            "title_tips": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "author_tips": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "cover_description": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "plot_details": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "additional_notes": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "quotes": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            ),
            "genre": forms.CheckboxSelectMultiple(),
            "part_of_series": forms.NullBooleanSelect(),
        }

    def clean(self):
        super().clean()
        if not any(
            (
                self.cleaned_data["plot_details"],
                self.cleaned_data["quotes"],
                self.cleaned_data["cover_description"],
            )
        ):
            raise forms.ValidationError(
                "You must fill at least one of the following fields: Plot details, Quotes or Cover description!"
            )

        if form_empty:
            raise forms.ValidationError("You must fill at least one field!")
