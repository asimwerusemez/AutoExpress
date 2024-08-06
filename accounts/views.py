from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import ConnexionForm, CreateUserForm

from django.contrib import messages


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
        else:
            form = CreateUserForm(request.POST)
    return render(request, "accounts/register.html", {"form":form})


def login_user(request):
    form = ConnexionForm(request.POST)
    if request.method == "POST":
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("car:cars_view")
            else:
                messages.error(request, "Identifiants invalides. Veuillez réessayer.")
                form = ConnexionForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('accounts:login')
