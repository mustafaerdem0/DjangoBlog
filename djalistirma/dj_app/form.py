from django import forms

from .models import Notes
from django.contrib.auth.models import User


class notupdate(forms.ModelForm):
        class Meta:
            model = Notes
            fields = ['note_title','note_content','note_image','note_url']


class formprofile(forms.ModelForm):
      class Meta:
            model= User
            fields = ['username','first_name','last_name']
            help_texts = {  
                "username": None
            }
            
       