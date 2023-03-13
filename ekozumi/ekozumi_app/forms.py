"""
Forms that will be used on different pages in our app
Authors: Christian Wood, Oscar Klemenz
"""

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class SignUpForm(UserCreationForm):
    '''
    Form used when a user registers an account, uses inbuilt django UserCreationForm
    '''
    email = forms.EmailField(required=True)

    class Meta:
        '''
        Meta info about form
        '''
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        '''
        Removes some of the help text for logging in django automatically uses
        '''
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ZumiCreationForm(forms.Form):
    '''
    Used for creating a new zumi, when a player creates an account
    '''
    petName = forms.CharField(label="Zumi name", max_length=50)
    petType = forms.CharField(max_length=9, label='Zumi type',
                              widget=forms.RadioSelect(choices=PET_CHOICES), initial='HEDGEHOG'  )
    
    class Meta:
        '''
        Meta info about form
        '''
        model = Pet
        fields = ('petName', 'petType')
