from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("notes")
        else:
            print("Error auth form validation")
    form = RegistrationForm()
    return render(request, "registration_user.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("notes")
    form = LoginForm()
    return render(request, "login_user.html", context={"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("notes")
