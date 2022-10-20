from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.user_logout,name='logout'),
]

