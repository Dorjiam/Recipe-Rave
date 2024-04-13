from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

global_dict: dict = {
    "user_logged_in": False
}


def index(response):
    return HttpResponseRedirect("/home")


def home(response):
    return render(response, "home.html", global_dict)


def login(response):
    return render(response, "login.html", global_dict)


def sign_up(response):
    return render(response, "sign-up.html", global_dict)


def user(response, name):
    return render(response, "user.html", global_dict.update({"username": name}))
