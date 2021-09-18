from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Profile,Comment
from .forms import ProfileForm,CommentForm

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
def profile_new(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect('profile_edit')
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()
    args = {
        'form': form,
    }
    return render(request, 'profiles/profile_edit.html', args)


@login_required
def profile_edit(request):
    if not Profile.objects.filter(user=request.user).exists():
        return redirect('profile_new')
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.name = form.cleaned_data['name']
            profile.bio = form.cleaned_data['bio']
            profile.image = form.cleaned_data['image']
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    args = {
        'form': form,
    }
    return render(request, 'profiles/profile_edit.html', args)

@login_required
def add_comment_to_profile(request,pk):
    post = get_object_or_404(Profile,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('profile_detail',pk=post.pk)

    else:
        form = CommentForm()

    return render(request,'profiles/comment_form.html',{'form':form})

@login_required
def report_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('profile_detail',pk=post_pk)
