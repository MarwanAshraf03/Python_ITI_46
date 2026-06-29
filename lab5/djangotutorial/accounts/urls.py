# from django.contrib import admin
# from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path("login_user/", views.login_user, name="login_user"),
    path("signup_user/", views.signup_user, name="signup_user"),
]
