"""
Admin.py is used to register models on the admin panel,
this will then allow gamekeepers to access these models and
modify them.

This allows game keepers to create daily challenges,
and sustainablility dialogue for monster battles
"""

from django.contrib import admin
from .models import Profile, Pet, Monster, Location, Megaboss

# Models which are displayed in the admin panel
# Register your models here.
admin.site.register(Profile)
admin.site.register(Pet)
admin.site.register(Monster)
admin.site.register(Location)
admin.site.register(Megaboss)
