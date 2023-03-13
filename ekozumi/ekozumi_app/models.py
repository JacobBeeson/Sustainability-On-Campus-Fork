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
    '''
    Contains info about each User's pet
    '''
    petID = models.AutoField(primary_key=True)
    petName = models.CharField(max_length=50)
    lastFed = models.DateTimeField(default=django.utils.timezone.now())
    petType = models.CharField(max_length=9, choices=PET_CHOICES)

    def __str__(self):
        return self.petName

class Profile(models.Model):
    '''
    Additional information for each user, one to one
    relationship with each User model, auto created
    upon registration
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    petID = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Monster(models.Model):
    '''
    Contains info about each monster
    '''
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
     '''
     Contains info about each location
     '''
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
    '''
    When a user is created, a profile is also created
    '''
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()