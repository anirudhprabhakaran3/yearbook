from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm

# Create your views here.

def index(request):
    users_count = User.objects.all().count() - 1
    args = {
        'users_count': users_count,
    }
    return render(request, 'profiles/index.html', args)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profiles_home')
    else:
        form = UserCreationForm()
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
                return redirect('profiles_home')
    else:
        form = AuthenticationForm()
    args = {
        'form': form
    }
    return render(request, 'profiles/login.html', args)


@login_required
def profile_home(request):
    profiles = Profile.objects.all().order_by('name')
    args = {
        'profiles': profiles,
    }
    return render(request, 'profiles/profile_home.html', args)

@login_required
def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    args = {
        'profile': profile,
    }
    return render(request, 'profiles/profile_detail.html', args)

@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            try:
                profile = Profile.objects.get(user=user)
                profile.name = form.cleaned_data['name']
                profile.bio = form.cleaned_data['bio']
                profile.save()
            except Profile.DoesNotExist:
                name = form.cleaned_data['name']
                bio = form.cleaned_data['bio']
                profile = Profile.objects.create(user=user, name=name, bio=bio)
                profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        try:
            profile = Profile.objects.get(user=user)
            form = ProfileForm(instance=profile)
        except Profile.DoesNotExist:
            form = ProfileForm()
    args = {
        'form': form
    }
    return render(request, 'profiles/profile_edit.html', args)
