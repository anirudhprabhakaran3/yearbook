from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    users_count = User.objects.all().count() - 1
    args = {
        'users_count': users_count,
    }
    return render(request, 'profiles/index.html', args)

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('profiles_home')
    args = {
        'form': form,
    }
    return render(request, 'profiles/signup.html', args)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are logged in!")
                return redirect('profiles_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    args = {
        'form': form
    }
    return render(request, 'profiles/login.html', args)


@login_required
def profile_home(request):
    return render(request, 'profiles/profile_home.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("index")
