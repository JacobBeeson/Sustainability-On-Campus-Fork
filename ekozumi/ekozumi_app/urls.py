from django.urls import path
from . import views

# Currently 127.0.0.1:8000/ekozumi/ will go to the login page
urlpatterns = [
    path("", views.login, name="ekozumi-login"),
    path("register/", views.register, name="ekozumi-register")
]