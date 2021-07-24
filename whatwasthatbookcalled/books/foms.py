from django import forms
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
        }
