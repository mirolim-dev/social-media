import django


from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from users.models import User

from .forms import RegisterForm
# Create your views here.

def home(request):
    user = request.user
    # user = User.objects.get(username=request.user.username)
    posts = user.get_posts_by_followings(2)
    print(user, posts)
    return render(request, 'index.html')



def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'setting.html')


def sign_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('login')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
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


def follow(request, pk):
    user = request.user
    user1 = User.objects.get(id=pk)
    user1.followings.add(user)
    user.followers.add(user1)
    user.save()
    user1.save()
    return redirect('home')