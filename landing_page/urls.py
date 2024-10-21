from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name = "register"),
    path("/login", views.login, name = "login"),
    path("/forget_pass", views.forget_pass, name = "forget_pass"),
]