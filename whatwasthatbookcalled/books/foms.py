from django import forms
from django.forms.widgets import CheckboxInput, Select
from whatwasthatbookcalled.books.models import Book, BookGenre, Comment
from languages import languages
from django.utils.safestring import mark_safe


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["solved", "filled_fields_count", "user"]

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


class FilterSortForm(forms.Form):
    GENRES_CHOICES = [(x.id, x.name) for x in BookGenre.objects.all()]
    SOVED_CHOICES = ((None, "Status"), (True, "Solved"), (False, "Not solved"))
    SORT_CHOICES = (
        ("date", "Posting date"),
        ("popularity", "Popularity"),
        ("info-amount", "Amount of information provided"),
    )

    language = forms.ChoiceField(
        required=False,
        choices=[("", "Language")] + languages,
        widget=Select(attrs={"onchange": "this.form.submit();"}),
        label="",
    )
    genre = forms.ChoiceField(
        required=False,
        choices=[("", "Genre")] + GENRES_CHOICES,
        widget=Select(attrs={"onchange": "this.form.submit();"}),
        label="",
    )
    solved = forms.BooleanField(
        required=False,
        widget=Select(choices=SOVED_CHOICES, attrs={"onchange": "this.form.submit();"}),
        label="",
    )

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        widget=Select(attrs={"onchange": "this.form.submit();"}),
        required=False,
        label_suffix="",
    )
    reverse_order = forms.BooleanField(
        widget=CheckboxInput(attrs={"onchange": "this.form.submit();"}),
        required=False,
        label=mark_safe('<i class="fas fa-sort"></i>'),
        label_suffix="",
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        labels = {"text": ""}
        widgets = {
            "text": forms.Textarea(
                attrs={"rows": 3, "cols": 50, "placeholder": "Add a comment..."}
            )
        }
