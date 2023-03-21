"""
Defines the forms which will be used in our application

Authors: Christian Wood, Oscar Klemenz
"""

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Pet, PET_CHOICES

class SignUpForm(UserCreationForm):
    """
    - Form for registering users
    - Displayed on register.html

    Args:
        UserCreationForm (form): Inbuilt django registration form
    Attributes:
        Email (String) : Email of the new user
        (Inbuilt) Username : Username decided by user
        (Inbuilt) Password1 : Chosen password of user
        (Inbuilt) Password2 : Confirms user has entered correct password
    """

    email = forms.EmailField(required=True)

    class Meta:
        """
        - Meta information about this form, model is set to User as we
          are using a django auth model for registering users.
        - Contains the fields, which will be shown to the user
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        """
        Custom __init__, to remove the help text django automatically uses
        in login forms
        """
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ZumiCreationForm(forms.Form):
    """
    - Form for creating a new zumi for a user
    - Displayed on zumi_creation.html

    Args:
        forms : Form which the user fills out, which data is processed
                from.
    Attributes:
        petName (CharField) : Name of users zumi
        petType (CharField) : Type of zumi, defined by PET_CHOICES dictionary
    """

    petName = forms.CharField(label="Zumi name", max_length=50)
    petType = forms.CharField(max_length=9, label='Zumi type',
                              widget=forms.RadioSelect(choices=PET_CHOICES), initial='HEDGEHOG'  )

    class Meta:
        """
        - Meta information about this form, model is set to Pet,
          a custom model created in .models
        - Contains the fields, which will be shown to the user (petName and petType)
        """
        model = Pet
        fields = ('petName', 'petType')
