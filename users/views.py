# Create your views here.
from django.contrib.auth import authenticate, login as dj_login
from django.shortcuts import redirect, render

from users.forms import RegisterForm, LoginForm


def register(request):
    msg = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "Пользователь создан..."
            return redirect("login")
        else:
            msg = "Ой, кажется ошибка. Пожалуйста, проверьте корректность заполнения полей."
    else:
        form = RegisterForm()
    return render(
        request,
        "users/register.html",
        {"form": form, "msg": msg, "title": "Регистрация"},
    )


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None and user.role == "freelancer":
                dj_login(request, user)
                return redirect("freelancer")
            elif user is not None and user.role == "customer":
                dj_login(request, user)
                return redirect("customer")
            else:
                msg = "Неверные учетные данные"
        else:
            msg = "Ой, кажется ошибка. Пожалуйста, проверьте корректность заполнения полей."
    return render(
        request, "users/login.html", {"form": form, "msg": msg, "title": "Вход"}
    )


# @login_required
# def custom_logout(request):
#     msg = None
#     logout(request)
#     msg = "Logged out successfully!"
#     return redirect("home")


def freelancer(request):
    return render(
        request, "users/freelancer.html", {"title": "Личный кабинет фрилансера"}
    )


def customer(request):
    return render(request, "users/customer.html", {"title": "Личный кабинет клиента"})


def profile(request):
    return render(request, "users/profile.html", {"title": "Профиль"})
