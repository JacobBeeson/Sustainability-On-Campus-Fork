"""
Views load HTML webpages, and perform any logic needed for post requests
and displaying user specific information

Authors: Christian Wood, Oscar Klemenz
"""

from django.shortcuts import render, redirect
from .forms import SignUpForm, ZumiCreationForm
from .models import Pet, Monster, Location, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import django.utils.timezone
from datetime import datetime

ZUMI_IMAGES = {"Hedgehog":["Images/hedge-hog-happy.png", "Images/hedge-hog-normal.png",
                           "Images/hedge-hog-sad.png"], "Badger":["Images/hedge-hog-happy.png",
                            "Images/hedge-hog-normal.png", "Images/hedge-hog-sad.png"], "Frog":["Images/frog-happy.png",
                            "Images/frog-normal.png", "Images/frog-sad.png"], "Bat":["Images/bat-happy.png",
                            "Images/bat-normal.png", "Images/bat-sad.png"], "Weasel":["Images/weasel-happy.png",
                            "Images/weasel-normal.png", "Images/weasel-sad.png"], "Rabbit":["Images/rabbit-happy.png",
                            "Images/rabbit-normal.png", "Images/rabbit-sad.png"]}
BADDIE_IMAGES = {"Ciggy":["Images/ciggy-normal.png", "Images/ciggy-angry.png"], "Pipe":["Images/pipe-normal.png",
                        "Images/pipe-angry.png"]}

# Default monster is used if a game keeper has not created a monster for a given day
defaultMonster = Monster(monsterName="placeholder", monsterImage="Images/ciggy-normal.png",
                         monsterAngryImage="Images/ciggy-angry.png", monsterIntroDialogue="Enemy Placeholder",
                         playerIntroDialogue="Player placeholder", monsterOutroDialogue="Enemy Placeholder",
                         playerOutroDialogue="Player placeholder")
# Default location is used if a game keeper has not created a location for a given day
defaultLocation = Location(locationName="Innovation",
                           minLatitude=50, maxLatitude=55, minLongitude=40, maxLongitude=45,
                           locationHint="Get Innovative", anagramWord="Forestry")

def registrationPage(request):
    """
    Contains the logic for when a user registers a new account
    Args:
        request (HttpRequest): Will either be a POST or GET request,
                                POST - User account needs to be created
                                GET  - Load registration form
    Returns:
        render() : When a new user is trying to register an account,
                   registration.html will load, if they are creating an
                   account their info will be processed, and redirected
                   to zumi_creation.html
    """
    if request.method == 'POST':
        # Processes the form
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('zumi_creation')
    else:
        form = SignUpForm()
    return render(request, 'ekozumi_app/register.html', {'form': form})

def logoutPage(request):
    """
    Logs user out of account and redirects to login page

    Args:
        request (HttpRequest)
    Returns:
        render() : Login page
    """
    logout(request)
    return redirect('login')

@login_required()
def homePage(request):
    """
    Home page of our application, displays the users zumi and
    how hungry the zumi is, based on its visual emotion

    Args:
        request (HttpRequest)
    Returns:
        render() : Home page
    """
    current_user = request.user
    current_zumi = current_user.profile.petID
    zumi_type = current_zumi.petType
    #if its been more than 48 hours since last fed zumi will be sad
    if current_zumi.lastFed + django.utils.timezone.timedelta(2) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][2]
    #if its been more than 24 hours since last fed zumi will be normal
    elif current_zumi.lastFed + django.utils.timezone.timedelta(1) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][1]
    #if its been under 24 hours since last fed zumi will be happy
    else:
        zumi_image = ZUMI_IMAGES[zumi_type][0]
    return render(request, "ekozumi_app/home.html", {'image_source':zumi_image})

@login_required()
def zumiCreationPage(request):
    """
    Contains the logic for when a user creates a new zumi
    Args:
        request (HttpRequest): Will either be a POST or GET request,
                                POST - Pet needs to be created
                                GET  - Load zumi creation form
    Returns:
        render() : When a new user is trying to create a pet,
                   zumi_creation.html will load, if they have
                   just created a pet, their info will be processed
                   and the home page will be loaded
    """
    if request.method == 'POST':
        form = ZumiCreationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Creates a new pet
            pet = Pet(petName = cleaned_data['petName'], petType = cleaned_data['petType'],)
            pet.save()
            # Links pet and user
            current_user = request.user
            current_user.profile.petID=pet
            current_user.save()

            return redirect('home_page')
    else:
        form = ZumiCreationForm()
    return render(request, "ekozumi_app/zumi_creation.html", {'form':form})

@login_required()
def puzzlePage(request):
    """
    Daily puzzle, loads the puzzle for today, which will have been
    generated by a game keeper on the admin page

    Args:
        request (HttpRequest)
    Returns:
        render() : puzzle.html, with the hint and anagram passed into the page
    """
    try:
        hint, anagramWord= Location.objects.values("locationHint", "anagramWord").get(dayOfAppearance = datetime.now().date())
     # If it doesn't exist uses a placeholder
    except Location.DoesNotExist:
        hint = defaultLocation.locationHint
        anagramWord = defaultLocation.anagramWord
    return render(request, "ekozumi_app/puzzle.html", {"hint":hint, "anagramWord":anagramWord})

@login_required()
def mapPage(request):
    """
    Page containing the map, which the user can use to navigate across campus
    to find sustainable locations provided in the hint.

    Args:
        request (HttpRequest)
    Returns:
        render() : map.html, passes in the users current zumi and the location of
                   the sustainable spot
    """
    current_user = request.user
    current_zumi = current_user.profile.petID
    zumi_type = current_zumi.petType
    try:
        location = Location.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
    except Location.DoesNotExist:
        location = defaultLocation
    #if its been more than 48 hours since last fed
    if current_zumi.lastFed + django.utils.timezone.timedelta(2) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][2]
    #if its been more than 24 hours since last fed
    elif current_zumi.lastFed + django.utils.timezone.timedelta(1) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][1]
    #if its been under 24 hours since last fed
    else:
        zumi_image = ZUMI_IMAGES[zumi_type][0]
    return render(request, "ekozumi_app/map.html", {'image_source':zumi_image, 'location':location})

@login_required()
def fightIntroPage(request):
    """
    Introduction to the fight, against the environmental threat
    player will recieve dialogue about a sustainable issue

    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from map fightintro.html is rendered,
                   If they are tring to access the url from somewhere else in the
                   app they are redirected to the home page
    """
    # Checks the user has come from the map page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/map/"):
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        # Gets todays monster
        try:
            monster = Monster.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
        except Monster.DoesNotExist:
            monster = defaultMonster
        return render(request, "ekozumi_app/fightIntro.html", {'zumi_source':zumi_image, "monster":monster})
    else:
        return redirect('home_page')   

@login_required()
def fightOutroPage(request):
    """
    Outro dialogue for the fight

    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from the fight fightoutro.html is rendered,
                   If they are tring to access the url from somewhere else in the
                   app they are redirected to the home page
    """
    # Checks the user has come from the fight page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight/"):
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        # Gets todays monster
        try:
            monster = Monster.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
        except Monster.DoesNotExist:
            monster = defaultMonster
        return render(request, "ekozumi_app/fightOutro.html",
                      {'zumi_source':zumi_image, "monster":monster})
    else:
        return redirect('home_page')

@login_required()
def fightPage(request):
    """
    Whack a mole fight against the enemy

    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from the fight intro whack-a-mole.html is rendered,
                   If they are tring to access the url from somewhere else in the
                   app they are redirected to the home page
    """
    # Checks user has come from the fight intro page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight_intro/"):
        # Gets todays monster
        try:
            monster = Monster.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
        except Monster.DoesNotExist:
            monster = defaultMonster
        return render(request, "ekozumi_app/whack-a-mole.html", {"monster":monster})
    else:
        return redirect('home_page')

@login_required()
def feedZumiPage(request):
    """
    Page updates the last time the user has fed their zumi,
    only allows the user to feed zumi if they have come from the
    fight outro page.

    Args:
        request (HttpRequest)
    Returns:
        render() : Redirects to home page once processing is finished
    """
    # Checks user has come from fight, and nowhere else
    # Stops zumi being fed at anytime
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight_outro/"):
        # Feeds zumi
        current_user = request.user
        current_user.profile.score += 5
        current_user.save()
        current_zumi = current_user.profile.petID
        current_zumi.lastFed = django.utils.timezone.now()
        current_zumi.save()
    return redirect('home_page')

@login_required()
def leaderboardPage(request):
    """
    Displays the top 10 scores of users across campus, scoring metric
    based upon how many times a user has fed their zumi.

    Args:
        request (HttpRequest)
    Returns:
        render() : leaderboard.html, with the top 10 scores
    """
    topscorers = Profile.objects.exclude(petID__isnull=True).order_by('-score')[0:10]
    return render(request, "ekozumi_app/leaderboard.html", {"topscorers":topscorers})
