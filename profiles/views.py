from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    users_count = User.objects.all().count() - 1
    args = {
        'users_count': users_count,
    }
    return render(request, 'profiles/index.html', args)