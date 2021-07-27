from django import forms
from django.db.models import QuerySet
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

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
        form_empty = True
        for field_value in self.cleaned_data.values():
            if (
                field_value is not None
                and field_value != ""
                and not (isinstance(field_value, QuerySet) and len(field_value) == 0)
            ):
                form_empty = False
                break

        if form_empty:
            raise forms.ValidationError("You must fill at least one field!")
