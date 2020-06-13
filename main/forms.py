from django import forms 
from .models import Profile, File
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields=['name','file']
class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=256, required=False,help_text='Optional')
    last_name=forms.CharField(max_length=256, required=False, help_text='Optional')
    email=forms.EmailField(max_length=256, help_text="Required.")
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1','password2']