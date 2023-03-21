"""
Views load HTML webpages, and perform any logic needed for post requests
and displaying user specific information
Authors: Christian Wood, Oscar Klemenz
"""

from django.shortcuts import render, redirect
from .forms import SignUpForm, ZumiCreationForm
from .models import Pet, Monster, Megaboss, Location, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import logout
from urllib.parse import urlparse
import django.utils.timezone
from datetime import datetime

# Images of all different zumis, with their different emotions
ZUMI_IMAGES = {"Hedgehog":["Images/hedge-hog-happy.png", "Images/hedge-hog-normal.png", "Images/hedge-hog-sad.png"],
               "Fox":["Images/fox-happy.png", "Images/fox-normal.png", "Images/fox-sad.png"],
               "Frog":["Images/frog-happy.png", "Images/frog-normal.png", "Images/frog-sad.png"],
               "Rabbit":["Images/rabbit-happy.png", "Images/rabbit-normal.png", "Images/rabbit-sad.png"],
               "Bluetit":["Images/bluetit-happy.png", "Images/bluetit-normal.png", "Images/bluetit-sad.png"]}
# Hunger bar images, used on the homePage
HUNGER_IMAGES = ["Images/full_hunger.png","Images/half_hunger.png","Images/empty_hunger.png"]

# Default monster is used if a game keeper has not created a monster for a given day
defaultMonster = Monster(monsterName="placeholder", monsterImage="Images/ciggy-normal.png",
                         monsterAngryImage="Images/ciggy-angry.png", monsterIntroDialogue="Enemy Placeholder",
                         playerIntroDialogue="Player placeholder", monsterOutroDialogue="Enemy Placeholder",
                         playerOutroDialogue="Player placeholder")
# Default megaboss is used if a game keeper has not created a megaboss for a given day
defaultMegaboss = Megaboss(megabossName="Placeholdermegaboss", megabossImage="Images/cigarette-megaboss-normal.png",
                         megabossAngryImage="Images/cigarette-megaboss-angry.png", megabossIntroDialogue="Enemy Placeholder",
                         megabossOutroDialogue="Enemy Placeholder", megabossQ1="Question 1", megabossQ1CA="Correct answer",
                         megabossQ1WA1="Incorrect 1", megabossQ1WA2="Incorrect 2", megabossQ1WA3="Incorrect 3",
                         megabossQ2="Question 2", megabossQ2CA="Correct answer", megabossQ2WA1="Incorrect 1", 
                         megabossQ2WA2="Incorrect 2", megabossQ2WA3="Incorrect 3", megabossQ3="Question 3",
                         megabossQ3CA="Correct answer", megabossQ3WA1="Incorrect 1", megabossQ3WA2="Incorrect 2",
                         megabossQ3WA3="Incorrect 3", megabossQ4="Question 4", megabossQ4CA="Correct answer",
                         megabossQ4WA1="Incorrect 1", megabossQ4WA2="Incorrect 2", megabossQ4WA3="Incorrect 3",
                         timesFought=0, averageTime=0, averageAttempts=0)
# Default location is used if a game keeper has not created a location for a given day
defaultLocation = Location(locationName="Weekend",
                           minLatitude=50, maxLatitude=55, minLongitude=40, maxLongitude=45,
                           locationHint="Wait until monday for the next hint", anagramWord="Forestry")

def registrationPage(request):
    """
    Displays user registration form for new users, manages POST requests when
    user creates a new account. Also deals with emailing users a confirmation email.

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

            # Save the new user profile to database
            user.save()
            raw_password = form.cleaned_data.get('password1')
            
            #send welcome email
            subject = 'Welcome to Ekozumi!'
            message = 'Your account has been registered with Ekozumi, have fun exploring!'
            from_email = 'ekozumiap@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

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
    how hungry the zumi is, based on its visual emotion and hunger bar

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
        zumi_hunger = HUNGER_IMAGES[2]
    #if its been more than 24 hours since last fed zumi will be normal
    elif current_zumi.lastFed + django.utils.timezone.timedelta(1) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        zumi_hunger = HUNGER_IMAGES[1]
    #if its been under 24 hours since last fed zumi will be happy
    else:
        zumi_image = ZUMI_IMAGES[zumi_type][0]
        zumi_hunger = HUNGER_IMAGES[0]
    return render(request, "ekozumi_app/home.html", {'image_source':zumi_image,'hunger_image_source':zumi_hunger})

@login_required()
def zumiCreationPage(request):
    """
    Contains the logic for when a user creates a new zumi, checks for a POST
    request and creates a new PET model for the new user

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
    return render(request, "ekozumi_app/zumiCreation.html", {"form":form})

@login_required()
def puzzlePage(request):
    """
    Daily puzzle page, loads the puzzle for today, which will have been
    generated by a game keeper on the admin page

    Args:
        request (HttpRequest)
    Returns:
        render() : puzzle.html, with the hint and anagram passed into the page
    """
    try:
        location=Location.objects.get(dayOfAppearance = datetime.now().date())
        hint = location.locationHint
        anagramWord = location.anagramWord
     # If it doesn't exist uses a placeholder
    except Location.DoesNotExist:
        hint = defaultLocation.locationHint
        anagramWord = defaultLocation.anagramWord
    return render(request, "ekozumi_app/puzzle.html", {"hint":hint, "anagramWord":anagramWord})

@login_required()
def mapPage(request):
    """
    Page containing the map, which the user can use to navigate across campus
    to find sustainable locations provided in the hint. Zumi dispayed 

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
    # Checks if battle has been completed today
    notFedToday = True
    if(current_zumi.lastFed.date() == django.utils.timezone.now().date()):
        notFedToday = False
    return render(request, "ekozumi_app/map.html", {'image_source':zumi_image, 'location':location, 'notFedToday':notFedToday})

@login_required()
def fightIntroPage(request):
    """
    Introduction to the fight, against the environmental threat
    player will recieve dialogue about a sustainable issue or be
    introduced to a megaboss if accessed on a Friday
    
    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from map fightintro.html is rendered,
                   If they are tring to access the url from somewhere else in the
                   app they are redirected to the home page
    """
    
    # Checks the user has come from the map page
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/map/"):
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        #checks if a megaboss is due
        if datetime.today().weekday() == 4:
            # Gets todays megaboss
            try:
                megaboss = Megaboss.objects.get(dayOfAppearance = datetime.now().date())
            # If it doesn't exist uses a placeholder
            except Megaboss.DoesNotExist:
                megaboss = defaultMegaboss
            return render(request, "ekozumi_app/megabossFightIntro.html", {'zumi_source':zumi_image, "megaboss":megaboss})
        else:
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
def fightPage(request):
    """
    Whack a mole fight against the enemy or a megaboss battle
    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from the fight intro whack-a-mole.html or 
        megabossFight.htmlare rendered. If they are trying to access the url from
        somewhere else in the app they are redirected to the home page
    """
    # Checks user has come from the fight intro page
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight_intro/" or previous_path ==  "/ekozumi/lose/"):
        #checks if a megaboss is due
        if datetime.today().weekday() == 0:
            # Gets todays megaboss
            try:
                megaboss = Megaboss.objects.get(dayOfAppearance = datetime.now().date())
            # If it doesn't exist uses a placeholder
            except Megaboss.DoesNotExist:
                megaboss = defaultMegaboss
            return render(request, "ekozumi_app/megabossFight.html", {"megaboss":megaboss})
        else:
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
def fightOutroPage(request):
    """
    Outro dialogue for the fight
    Args:
        request (HttpRequest)
    Returns:
        render() : If user has come from the fight fightOutro.html or 
        megabossFightOutro.html are rendered. If they are tring to access
        the url from somewhere else in the app they are redirected to the home page
    """
    # Checks the user has come from the fight page
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight/"):
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        # Gets todays monsters
        try:
            monster = Monster.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
        except Monster.DoesNotExist:
            monster = defaultMonster
        return render(request, "ekozumi_app/fightOutro.html", {'zumi_source':zumi_image, "monster":monster})
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
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight_outro/"):
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

@login_required()
def losePage(request):
    """
    Page for when a player loses, allows players to
    restart boss battle or return to home page.
    Can only be accessed from fight.html
    Args:
        request (HttpRequest)

    Returns:
        redirect(): If player comes from /fight/ they are redirected to
                    you youLose.html if not they return to home page
    """
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight/"):
        return render(request, "ekozumi_app/youLose.html")
    else:
        return redirect('home_page')

@login_required()
def uploadMonsterDataPage(request):
    """
    Uploads users score to the database, and feeds their zumi
    once the monster has been defeated.
    Args:
        request (HttpRequest)
    """
        # Checks the user has come from the fight page
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight/"):
        # Get http request, print it
        score = int(request.POST.get('score'))
        current_user = request.user
        current_user.profile.score += score
        current_user.save()
        return redirect('home_page')
    else:
        return redirect('home_page')

@login_required()
def uploadMegabossDataPage(request):
    """
    Uploads users score and time to the database, and feeds their zumi
    once the megaboss has been defeated.
    Args:
        request (HttpRequest)
    """
    # Checks the user has come from the fight page
    previous_url = request.META.get('HTTP_REFERER')
    previous_path = urlparse(previous_url).path
    if( previous_path == "/ekozumi/fight/"):
        # Get http request, print it
        score = int(request.POST.get('score'))
        attempts = int(request.POST.get('attempts'))
        seconds = int(request.POST.get('seconds'))

        try:
            megaboss = Megaboss.objects.get(dayOfAppearance = datetime.now().date())
        # If it doesn't exist uses a placeholder
        except Megaboss.DoesNotExist:
            megaboss = defaultMegaboss

        megaboss.averageAttempts = (megaboss.averageAttempts*megaboss.timesFought + attempts)/(megaboss.timesFought+1)
        megaboss.averageTime = (megaboss.averageTime*megaboss.timesFought + seconds)/(megaboss.timesFought+1)
        megaboss.timesFought += 1
        megaboss.save()

        current_user = request.user
        current_user.profile.score += score
        current_user.save()

        current_zumi = current_user.profile.petID
        current_zumi.lastFed = django.utils.timezone.now()
        current_zumi.save()

        return redirect('home_page')
    else:
            return redirect('home_page')