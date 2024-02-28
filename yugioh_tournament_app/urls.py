from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.main, name="main"),
    path("register/", views.register, name="register"),
]
