from django.shortcuts import redirect, render

from .forms import RegisterForm
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
    form = RegisterForm() 
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
            return redirect('home')
        else:
            print('data is not valid')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def account_settings(request):
    return render(request, 'account-setting.html')