from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profiles/', views.profile_home, name='profiles_home'),
    path('profiles/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profiles/new', views.profile_new, name='profile_new'),
    path('profiles/edit', views.profile_edit, name='profile_edit'),
    path('profiles/<int:pk>/comment/',views.add_comment_to_profile,name='add_comment_to_profile'),
    path('comment/<int:pk>/report',views.report_comment,name='report_comment'),
]
