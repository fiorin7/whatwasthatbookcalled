from django import forms
from django.forms.widgets import CheckboxInput, Select
from whatwasthatbookcalled.books.models import Book, BookGenre, Comment
from languages import languages
from django.utils.safestring import mark_safe


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Book
        exclude = ["solved", "filled_fields_count", "user"]

        widgets = {
            "title_tips": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "e.g. Something about ships.",
                },
            ),
            "author_tips": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "e.g. Last name started with 'S'.",
                },
            ),
            "cover_description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "e.g. Photo of a castle.",
                }
            ),
            "plot_details": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "e.g. A group of people was trying to destroy a ring.",
                }
            ),
            "additional_notes": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "e.g. I got the book from a thrift shop in Spain.",
                }
            ),
            "quotes": forms.Textarea(
                attrs={
                    "rows": 2,
                    "placeholder": "e.g. 'There is some good in this world, and it's worth fighting for.'",
                }
            ),
            "genre": forms.CheckboxSelectMultiple(),
            "part_of_series": forms.NullBooleanSelect(),
            "year_read": forms.NumberInput(attrs={"placeholder": "e.g. 1997"}),
            "year_written": forms.NumberInput(attrs={"placeholder": "e.g. 1874"}),
        }

        help_texts = {
            "title_tips": "Anything you can remember about the title.",
            "author_tips": "Anything you can remember about the author.",
            "language": "In which language did you read the book?",
            "year_written": "When approximately do you think the book was written?",
            "year_read": "When approximately did you read or see the book?",
            "part_of_series": "Was the book a part of series?",
            "cover_description": "What was on the cover?",
            "genre": "What genre was the book?",
            "plot_details": "Anything you can remember about the plot.",
            "quotes": "Any quotes that you can remember.",
            "additional_notes": "",
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        GENRES_CHOICES = [(x.id, x.name) for x in BookGenre.objects.all()]
        self.fields["genre"].choices = [("", "Genre")] + GENRES_CHOICES

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
        choices=[],
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
                attrs={"rows": 5, "cols": 60, "placeholder": "Add a comment..."}
            )
        }
