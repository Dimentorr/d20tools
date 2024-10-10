from django.shortcuts import render

# Create your views here.


def user_account(request):
    return render(request, 'personal_account/account.html')