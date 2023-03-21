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
FOX = "Fox"
FROG = "Frog"
RABBIT = "Rabbit"
BLUETIT = "Bluetit"

PET_CHOICES = [(HEDGEHOG,"Hedgehog"), (FOX, "Fox"),
               (FROG, "Frog"), (RABBIT, "Rabbit"), (BLUETIT, "Bluetit"),]

class Pet(models.Model):
    """
    This model represents a players zumi

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

class Megaboss(models.Model):
    """
    - Megaboss database model
    - Used in fightIntro.html, megabossFight.html, fightOutro.html

    Args:
        models.Model : Used to define each field
    Attributes:
        megabossID (AutoField)            : Primary key of megaboss,
                                           automatically created on instantiation
        megabossName (CharField)          : Name of megaboss
        dayOfAppearance (DateField)      : Day megaboss will appear for battle,
                                           only one megaboss can appear per week
        megabossImage (CharField)         : Path to megaboss image
        megabossAngryImage (CharField)    : Path to megaboss angry image
        megabossIntroDialogue (CharField) : Sustainable dialogue, about megaboss
        megabossOutroDialogue (CharField) : megaboss after defeat text
        megabossQ1 : Question one
        megabossQ1CA : Q1 correct answer
        megabossQ1WA1 : Q1 wrong answer 1
        megabossQ1WA2 : Q1 wrong answer 2
        megabossQ1WA3 : Q1 wrong answer 3
        megabossQ2 : Question two
        megabossQ2CA : Q2 correct answer
        megabossQ2WA1 : Q2 wrong answer 1
        megabossQ2WA2 : Q2 wrong answer 2
        megabossQ2WA3 : Q2 wrong answer 3
        megabossQ3 : Question three
        megabossQ3CA : Q3 correct answer
        megabossQ3WA1 : Q3 wrong answer 1
        megabossQ3WA2 : Q3 wrong answer 2
        megabossQ3WA3 : Q3 wrong answer 3
        megabossQ4 : Question four
        megabossQ4CA : Q4 correct answer
        megabossQ4WA1 : Q4 wrong answer 1
        megabossQ4WA2 : Q4 wrong answer 2
        megabossQ4WA3 : Q4 wrong answer 3
        timesFought : number of times fought
        averageTime : average time taken for each fight
        averageAttempts : average attempts taken for each fight
    Returns:
        String : Displays name of megaboss on admin site
    """

    megabossID = models.AutoField(primary_key=True)
    megabossName = models.CharField(max_length=50)
    dayOfAppearance = models.DateField(unique=True)
    megabossImage = models.CharField(max_length=50)
    megabossAngryImage = models.CharField(max_length=50)
    megabossIntroDialogue = models.CharField(max_length=500)
    megabossOutroDialogue = models.CharField(max_length=500)
    megabossQ1 = models.CharField(max_length=500)
    megabossQ1CA = models.CharField(max_length=500)
    megabossQ1WA1 = models.CharField(max_length=500)
    megabossQ1WA2 = models.CharField(max_length=500)
    megabossQ1WA3 = models.CharField(max_length=500)
    megabossQ2 = models.CharField(max_length=500)
    megabossQ2CA = models.CharField(max_length=500)
    megabossQ2WA1 = models.CharField(max_length=500)
    megabossQ2WA2 = models.CharField(max_length=500)
    megabossQ2WA3 = models.CharField(max_length=500)
    megabossQ3 = models.CharField(max_length=500)
    megabossQ3CA = models.CharField(max_length=500)
    megabossQ3WA1 = models.CharField(max_length=500)
    megabossQ3WA2 = models.CharField(max_length=500)
    megabossQ3WA3 = models.CharField(max_length=500)
    megabossQ4 = models.CharField(max_length=500)
    megabossQ4CA = models.CharField(max_length=500)
    megabossQ4WA1 = models.CharField(max_length=500)
    megabossQ4WA2 = models.CharField(max_length=500)
    megabossQ4WA3 = models.CharField(max_length=500)
    timesFought = models.IntegerField(default=0)
    averageTime = models.IntegerField(default=0)
    averageAttempts = models.IntegerField(default=0)
    
    def __str__(self):
        return self.megabossName

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
