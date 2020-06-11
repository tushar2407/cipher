from django import forms 
from .models import Profile, File
class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields=['name','file']