from django.urls import path, include
from .views import  (
    home, 
    UserLogin, 
    UploadFile,
    signup
)

urlpatterns=[
    #path('upload/', upload,name="upload" ),
    path('',home, name="home"),
    path('login/', UserLogin.as_view(), name="login"),
    path('upload/',UploadFile.as_view(),name="uploadFile"),
    path('register/',signup,name="signup")
]