from django.urls import path, include
from .views import upload, home, User
urlpatterns=[
    path('upload/', upload,name="upload" ),
    path('',home, name="home"),
    path('login/', User.as_view(), name="login")
]