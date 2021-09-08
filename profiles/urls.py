from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('profiles/', views.profile_home, name='profiles_home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]