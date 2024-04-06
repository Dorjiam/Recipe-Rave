from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.sign_up, name="sign_up"),
    path("user/<str:name>", views.user, name="user"),
]
