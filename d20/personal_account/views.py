from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'personal_account/register.html', {'form': form})


def logout_account(request):
    logout(request)
    return redirect('home')


def user_account(request):
    return render(request, 'personal_account/account.html')
