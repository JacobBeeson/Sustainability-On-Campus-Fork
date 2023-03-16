"""
Defines the models for our database
Authors: Christian Wood, Olivia Kerschen, Oscar Klemenz
"""

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import django.utils.timezone

# Possible choices for a users pet
HEDGEHOG = "Hedgehog"
BADGER = "Badger"
FROG = "Frog"
BAT = "Bat"
WEASEL = "Weasel"
RABBIT = "Rabbit"

PET_CHOICES = [(HEDGEHOG,"Hedgehog"), (BADGER, "Badger"),
               (FROG, "Frog"), (BAT, "Bat"), (WEASEL, "Weasel"), (RABBIT, "Rabbit"),]

class Pet(models.Model):
    """
    Players zumi

    Args:
        models.Model : Used to define each field
    Attributes:
        petID (AutoField)       : Primary key of pet, automatically created when
                                  a new pet is created.
        petName (CharField)     : User defined, name of their chosen pet
        lastFed (DateTimeField) : Datetime of when zumi  was last fed, attribute
                                  used in calculations to display how happy the zumi
                                  is.
        petType (CharField)     : Defined by PET_CHOICES dictionary, player has
                                  options of that dictionary for what kind of animal
                                  their pet is.
    Returns:
        String : Displays name of pet on admin site
    """

    petID = models.AutoField(primary_key=True)
    petName = models.CharField(max_length=50)
    lastFed = models.DateTimeField(default=django.utils.timezone.now()-django.utils.timezone.timedelta(1))
    petType = models.CharField(max_length=9, choices=PET_CHOICES)

    def __str__(self):
        return self.petName

class Profile(models.Model):
    """
    Additional information for each user, one to one
    relationship with each User model, auto created
    upon registration

    Args:
        models.Model : Used to define each field
    Attributes:
        user (OneToOneField) : Links Profile to User model
        score (IntegerField) : How many points the user has gained in game,
                               metric used in leaderboard
        petID (ForeignKey)   : Links Pet model to a User model
    Returns:
        String : Displays name of user on admin site
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    petID = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Monster(models.Model):
    """
    - Monster database model
    - Used in fightIntro.html, whack-a-mole.html, fightOutro.html

    Args:
        models.Model : Used to define each field
    Attributes:
        monsterID (AutoField)            : Primary key of monster,
                                           automatically created on instantiation
        monsterName (CharField)          : Name of monster
        dayOfAppearance (DateField)      : Day monster will appear for battle,
                                           only one monster can appear per day
        monsterImage (CharField)         : Path to monster image
        monsterAngryImage (CharField)    : Path to monster angry image
        monsterIntroDialogue (CharField) : Sustainable dialogue, about monster
        playerIntroDialogue (CharField)  : Player response before battle
        monsterOutroDialogue (CharField) : Monster after defeat
        playerOutroDialogue (CharField)  : Player victory text
    Returns:
        String : Displays name of monster on admin site
    """

    monsterID = models.AutoField(primary_key=True)
    monsterName = models.CharField(max_length=50)
    dayOfAppearance = models.DateField(unique=True)
    monsterImage = models.CharField(max_length=50)
    monsterAngryImage = models.CharField(max_length=50)
    monsterIntroDialogue = models.CharField(max_length=500)
    playerIntroDialogue = models.CharField(max_length=500)
    monsterOutroDialogue = models.CharField(max_length=500)
    playerOutroDialogue = models.CharField(max_length=500)

    def __str__(self):
        return self.monsterName

class Location(models.Model):
    """
    Locations of sustainable spots on campus,
    displayed on map.html

    Args:
        models.Model : Used to define each field
    Attributes:
        locationID (AutoField)      : Primary key of location,
                                      autocreated on instantiation
        locationName (CharField)    : Name of location, helps
                                      gamekeepers keep track of locations
        dayOfAppearance (DateField) : Only one location per day, appears
                                      on map.html
        minLongitude, maxLongitude, minLatitude, maxLatitude (FloatField) : Location ranges
        locationHint (CharField)    : Hint appears after anagram is completed
                                      on puzzle.html
        anagramWord (CharField)     : Word puzzle the user must solve each day,
                                      gamekeeper enters word which is then shuffled in
                                      puzzle.js, for the users to solve
    Returns:
        String : Displays name of location on admin site
    """


    locationID = models.AutoField(primary_key=True)
    locationName = models.CharField(max_length=50)
    dayOfAppearance = models.DateField(unique=True)
    minLongitude = models.FloatField()
    maxLongitude = models.FloatField()
    minLatitude = models.FloatField()
    maxLatitude = models.FloatField()
    locationHint = models.CharField(max_length=500)
    anagramWord = models.CharField(max_length=500)

    def __str__(self):
        return self.locationName

class AdminUser(models.Model):
    '''
    Possible way to implement admins for our application
    '''
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.username

@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    """
    When a user is created, a profile model is also
    setup for the user with a one to one relationship

    Args:
        sender (model): Which model the request has come from
        instance : User which has just registered
        created (Bool): If a user has just been created,
                        and requires a profile model to be setup
    """

    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
