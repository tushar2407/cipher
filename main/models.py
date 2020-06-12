from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
class File(models.Model):
    name=models.CharField(max_length=256)
    file=models.FileField(upload_to='files/')
    url=models.URLField(default="/")
    def __str__(self):
        return self.name
    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)
"""
class File(models.Model):
    name=models.CharField(max_length=256)
    file=models.FileField(upload_to='files/')
    #url=models.FilePathField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #cover=models.ImageField(default=NULL)
    def __str__(self):
        return self.name
    """def __init__(self, *args, **kwargs):
        self.user=user"""
    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    files=models.ManyToManyField(File)