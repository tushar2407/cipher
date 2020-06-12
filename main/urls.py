from django.urls import path, include
from .views import upload, home, UserLogin, UploadFile

urlpatterns=[
    #path('upload/', upload,name="upload" ),
    path('',home, name="home"),
    path('login/', UserLogin.as_view(), name="login"),
    path('upload/',UploadFile.as_view(),name="uploadFile")
]