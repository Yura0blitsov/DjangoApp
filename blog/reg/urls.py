from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.register, name='reg'),
    path('r', auth_views.LoginView.as_view()),
]