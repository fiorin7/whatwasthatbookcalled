from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from whatwasthatbookcalled.books_auth.forms import RegisterForm, LoginForm
from django.shortcuts import redirect, render


def sign_up(req):
    if req.method == "GET":
        form = RegisterForm()
        return render(req, "auth/register-login.html", {"form": form})

    form = RegisterForm(req.POST)

    if form.is_valid():
        form.save()
        return redirect("sign in")
    else:
        return render(req, "auth/register-login.html", {"form": form})


def sign_in(req):
    if req.method == "GET":
        form = LoginForm()
        return render(req, "auth/register-login.html", {"form": form, "sign_in": True})

    form = LoginForm(req, req.POST)
    if form.is_valid():
        login(req, form.user_cache)
        return redirect("/books")
    else:
        return render(req, "auth/register-login.html", {"form": form, "sign_in": True})


@login_required
def sign_out(req):
    logout(req)
    return redirect("/books")
