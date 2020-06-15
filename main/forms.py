from django import forms 
from .models import Profile, File
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields=['name','file']
class SignUpForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
    first_name=forms.CharField(max_length=256, required=False,help_text='Optional')
    last_name=forms.CharField(max_length=256, required=False, help_text='Optional')
    email=forms.EmailField(max_length=256, help_text="Required.")
    birth_date=forms.DateField(help_text="Required. Format: YYY-MM-DD")
    class Meta:
        model=User
        fields=['username', 'birth_date','first_name', 'last_name', 'email', 'password1','password2']