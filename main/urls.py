from django.urls import path, include
from .views import upload, home
urlpatterns=[
    path('upload/', upload,name="upload" ),
    path('',home, name="home")
]