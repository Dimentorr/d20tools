from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm


def register(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            errors = list()
            for field in form.errors:
                print(form.errors[field])
                if 'This field is required.' in form.errors[field].as_text():
                    errors.append(field + ' - Это поле обязательно к заполнению!')
                if 'The two password fields didn’t match.' in form.errors[field].as_text():
                    errors.append(field[:5] + ' - Пароли не совпадают!')
                if 'This password is too short.' in form.errors[field].as_text():
                    errors.append(field[:5] + ' - пароль слишком короткий!')
                if 'This password is too common' in form.errors[field].as_text():
                    errors.append(field[:5] + ' - пароль слишком простой!')
                if 'This password is too short. It must contain at least 8 characters.' in form.errors[field].as_text():
                    errors.append(field[:5] + ' - Пароль должен состоять не менее чем из 8 символов!')
                if 'This password is entirely numeric.' in form.errors[field].as_text():
                    errors.append(field[:5] + ' - Этот пароль полностью цифровой!')
            context['errors'] = errors
    else:
        form = UserRegisterForm()
    context['form'] = form
    return render(request, 'personal_account/register.html', context)


def logout_account(request):
    logout(request)
    return redirect('home')


def user_account(request):
    return render(request, 'personal_account/account.html')
