from django.shortcuts import render, redirect
from .forms import SignUpForm, ZumiCreationForm
from .models import Pet
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

ZUMI_IMAGES = {"Hedgehog":"Images/hedge-hog-normal.png", "Badger":"Images/hedge-hog-happy.png", "Frog":"Images/hedge-hog-happy.png", "Bat":"Images/hedge-hog-happy.png", "Weasel":"Images/hedge-hog-happy.png", "Rabbit":"Images/hedge-hog-happy.png"}
 
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
    zumi_type = current_user.profile.petID.petType
    print("static Images/" + ZUMI_IMAGES[zumi_type])
    return render(request, "ekozumi_app/home.html", {'image_source':ZUMI_IMAGES[zumi_type]})

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
    return render(request, "ekozumi_app/map.html")
