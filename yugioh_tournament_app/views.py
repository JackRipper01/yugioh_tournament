from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if "login" in request.POST:
            return HttpResponseRedirect("/yugioh_tournament_app/main/")
        elif "register" in request.POST:
            return HttpResponseRedirect("/yugioh_tournament_app/register/")

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request,user)
        #     return HttpResponseRedirect("/yugioh_tournament_app/main/")
        # else:
        #     context = {"error": "Failed to authenticate. Please try again."}
        #     return render(request, "yugioh_tournament_app/index.html", context)

    else:
        return render(request, "yugioh_tournament_app/index.html")


# VAMO MAURICIO IMMPLEMENTA AHI EL CHECKEADOR DE CONTRASEÑA ESE
def authenticate_personalizated(username, password):
    if User.objects.filter(username=username).exists() and mauricio_check_password(
        username, password
    ):
        return User.objects.get(username=username)
    else:
        return None


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            context = {"error": "Username already exists"}
            return render(request, "yugioh_tournament_app/register.html", context)
        else:
            # user = User.objects.create_user(username, password=mauricio_hash_password(password))
            user = User.objects.create_user(username, password=password)
            user.save()
            return HttpResponseRedirect("/yugioh_tournament_app/main/")
    else:
        return render(request, "yugioh_tournament_app/register.html")


# vamo alejandro implementa esta TALLA:
def main(request):
    return render(request, "yugioh_tournament_app/main.html")
