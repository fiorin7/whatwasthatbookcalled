from whatwasthatbookcalled.profiles.forms import (
    ProfileEditBioForm,
    ProfileEditProfilePictureForm,
)
from whatwasthatbookcalled.profiles.models import Profile
from django.shortcuts import redirect, render


def profile_base(
    req, profile_form, template_name, show_books=False, show_comments=False
):
    profile_obj = Profile.objects.get(user_id=req.user.id)
    date_joined_string = req.user.date_joined.strftime("%b %d, %Y")

    books = req.user.book_set.all()
    books_count = books.count()
    books = books.order_by("-last_modified")
    if not show_books:
        books = books[:3]

    comments = req.user.comment_set.all()
    comments = comments.order_by("-last_modified")
    comment_count = comments.count()
    solutions_count = comments.filter(is_solution=True).count()
    if not show_comments:
        comments = comments[:5]

    context = {
        "profile": profile_obj,
        "date_joined": date_joined_string,
        "username": req.user,
        "books": books,
        "books_count": books_count,
        "show_books": show_books,
        "comments": comments,
        "comment_count": comment_count,
        "solutions_count": solutions_count,
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
