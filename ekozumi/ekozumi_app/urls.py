"""
Defines all of the URL patterns for our application, in each path
the string is what should lead the URL 127.0.0.1:8000/ekozumi/
Authors: Christian Wood, Oscar Klemenz
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Currently 127.0.0.1:8000/ekozumi/ will go to the login page
urlpatterns = [
    path("register/", views.registrationPage, name="ekozumi-register"),
    path("", auth_views.LoginView.as_view(template_name='ekozumi_app/login.html'), name="login"),
    path("home/", views.homePage, name="home_page"),
    path("zumi_creation/", views.zumiCreationPage, name="zumi_creation"),
    path("puzzle/", views.puzzlePage, name="puzzle"),
    path("map/", views.mapPage, name="map"),
    path("logout/", views.logoutPage, name="logout"),
    path("fight_intro/", views.fightIntroPage, name="intro"),
    path("fight_outro/", views.fightOutroPage, name="outro"),
    path("fight/", views.fightPage, name="fight"),
    path("feed/", views.feedZumiPage, name="feed"),
    path("leaderboard/", views.leaderboardPage, name="leaderboard"),
]