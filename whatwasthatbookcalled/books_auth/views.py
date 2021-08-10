from django.contrib.auth import login, logout
from whatwasthatbookcalled.books_auth.forms import RegisterForm, LoginForm
from django.shortcuts import redirect, render


def sign_up(req):
    if req.method == "GET":
        form = RegisterForm()
        return render(req, "auth/register.html", {"form": form})

    form = RegisterForm(req.POST)
    print(form)

    if form.is_valid():
        form.save()
        return redirect("/books")
    else:
        return render(req, "auth/register.html", {"form": form})


def sign_in(req):
    if req.method == "GET":
        form = LoginForm()
        return render(req, "auth/register.html", {"form": form})

    form = LoginForm(req, req.POST)
    print(form)
    if form.is_valid():
        login(req, form.user_cache)
        return redirect("/books")
    else:
        return render(req, "auth/register.html", {"form": form})


def sign_out(req):
    logout(req)
    return redirect("/books")
