from django.shortcuts import render, redirect
from .forms import SignUpForm, ZumiCreationForm
from .models import Pet
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import django.utils.timezone 

"""
Views load HTML webpages, and perform any logic needed for post requests
and displaying user specific information
Authors: Christian Wood, Oscar Klemenz
"""

ZUMI_IMAGES = {"Hedgehog":["Images/hedge-hog-happy.png", "Images/hedge-hog-normal.png", "Images/hedge-hog-sad.png"], "Badger":["Images/hedge-hog-happy.png", "Images/hedge-hog-normal.png", "Images/hedge-hog-sad.png"], "Frog":["Images/frog-happy.png", "Images/frog-normal.png", "Images/frog-sad.png"], "Bat":["Images/bat-happy.png", "Images/bat-normal.png", "Images/bat-sad.png"], "Weasel":["Images/weasel-happy.png", "Images/weasel-normal.png", "Images/weasel-sad.png"], "Rabbit":["Images/rabbit-happy.png", "Images/rabbit-normal.png", "Images/rabbit-sad.png"]}
BADDIE_IMAGES = {"Ciggy":["Images/ciggy-normal.png", "Images/ciggy-angry.png"], "Pipe":["Images/pipe-normal.png", "Images/pipe-angry.png"]}

def registrationPage(request):
    '''
    Contains the logic for when a user registers
    '''
    # True when there is a post request
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

            # redirect user to zumi creation page
            return redirect('zumi_creation')
    else:
        form = SignUpForm()
    return render(request, 'ekozumi_app/register.html', {'form': form})

def logoutPage(request):
    '''
    Logs user out of account and redirects to login page
    '''
    logout(request)
    return redirect('login')

@login_required()
def homePage(request):
    current_user = request.user
    current_zumi = current_user.profile.petID
    zumi_type = current_zumi.petType
    #if its been more than 48 hours since last fed
    if current_zumi.lastFed + django.utils.timezone.timedelta(2) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][2]
    #if its been more than 24 hours since last fed
    elif current_zumi.lastFed + django.utils.timezone.timedelta(1) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][1]
    #if its been under 24 hours since last fed
    else:
        zumi_image = ZUMI_IMAGES[zumi_type][0]
    return render(request, "ekozumi_app/home.html", {'image_source':zumi_image})

@login_required()
def zumiCreationPage(request):
    '''
    View for creating as zumi
    '''
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
    return render(request, "ekozumi_app/puzzle.html")

@login_required()
def mapPage(request):
    """
    Page for map navigation
    """
    current_user = request.user
    current_zumi = current_user.profile.petID
    zumi_type = current_zumi.petType
    #if its been more than 48 hours since last fed
    if current_zumi.lastFed + django.utils.timezone.timedelta(2) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][2]
    #if its been more than 24 hours since last fed
    elif current_zumi.lastFed + django.utils.timezone.timedelta(1) < django.utils.timezone.now():
        zumi_image = ZUMI_IMAGES[zumi_type][1]
    #if its been under 24 hours since last fed
    else:
        zumi_image = ZUMI_IMAGES[zumi_type][0]
    return render(request, "ekozumi_app/map.html", {'image_source':zumi_image})
    
@login_required()
def fightIntroPage(request):
    """
    Intro to the fight
    """
    # Checks the user has come from the map page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/map/"):
        # Gets the correct images for the dialogue
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        baddie_image = BADDIE_IMAGES["Ciggy"][0]
        return render(request, "ekozumi_app/fightIntro.html", {'zumi_source':zumi_image, 'baddie_source':baddie_image})
    else:
        return redirect('home_page')

@login_required()
def fightOutroPage(request):
    """
    Outro dialogue for the fight
    """
    # Checks the user has come from the fight page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight/"):
        # Gets the correct images for the fight
        current_user = request.user
        current_zumi = current_user.profile.petID
        zumi_type = current_zumi.petType
        zumi_image = ZUMI_IMAGES[zumi_type][1]
        baddie_image = BADDIE_IMAGES["Ciggy"][0]
        return render(request, "ekozumi_app/fightOutro.html", {'zumi_source':zumi_image, 'baddie_source':baddie_image})
    else:
        return redirect('home_page')

@login_required()
def fightPage(request):
    """
    View for fight with enemy
    """
    # Checks user has come from the fight intro page
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight_intro/"):
        baddie_images = BADDIE_IMAGES["Ciggy"]
        return render(request, "ekozumi_app/whack-a-mole.html", {'baddie_normal_source':baddie_images[0], 'baddie_angry_source':baddie_images[1]})
    else:
        return redirect('home_page')

@login_required()
def feedZumiPage(request):
    """
    Page for feeding zumi after fight
    """
    # Checks user has come from fight, and nowhere else
    # Stops zumi being fed at anytime
    previous_url = request.META.get('HTTP_REFERER')
    if( previous_url == "http://127.0.0.1:8000/ekozumi/fight_outro/"):
        # Feeds zumi
        current_zumi = request.user.profile.petID
        current_zumi.lastFed = django.utils.timezone.now()
        current_zumi.save()
    
    return redirect('home_page')