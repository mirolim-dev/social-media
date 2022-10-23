from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')



def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'setting.html')


def sign_in(request):
    return render(request, 'signin.html')


def sign_up(request):
    return render(request, 'signup.html')


def account_settings(request):
    return render(request, 'account-setting.html')