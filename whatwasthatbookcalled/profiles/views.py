from whatwasthatbookcalled.profiles.forms import (
    ProfileEditBioForm,
    ProfileEditProfilePictureForm,
)
from whatwasthatbookcalled.profiles.models import Profile
import whatwasthatbookcalled.profiles.services as ProfileService
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def profile_base(
    req, profile_form, template_name, show_books=False, show_comments=False
):
    profile_obj = ProfileService.get_by_id(req.user.id)

    books = req.user.books
    if not show_books:
        books = books[:3]

    comments = req.user.comments
    if not show_comments:
        comments = comments[:5]

    context = {
        "profile": profile_obj,
        "books": books,
        "show_books": show_books,
        "comments": comments,
        "show_comments": show_comments,
    }

    if req.method == "GET":
        form = profile_form(instance=profile_obj)
        context["form"] = form

        return render(req, template_name, context)

    form = profile_form(req.POST, req.FILES, instance=profile_obj)
    context["form"] = form

    if form.is_valid():
        form.save()
        return redirect("profile")
    else:
        return render(req, template_name, context)


def profile(req, show_books=False, show_comments=False):
    profile_form = ProfileEditProfilePictureForm
    return profile_base(
        req, profile_form, "profiles/profile.html", show_books, show_comments
    )


def profile_show_all_books(req):
    return profile(req, show_books=True)


def profile_edit_bio(req):
    profile_form = ProfileEditBioForm
    return profile_base(req, profile_form, "profiles/profile-bio-edit.html")


def profile_show_all_comments(req):
    return profile(req, show_comments=True)
