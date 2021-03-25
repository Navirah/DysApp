#django

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#for user authentication
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


#for file uploads
class FileForm(forms.Form):
    picture=forms.ImageField()
