from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  FileForm
from .models import Profile, File
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
#from django.views.generic import TemplateView, LoginView
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponseRedirect
#@login_required(login_url='login/', redirect_field_name='redirect_to')
def upload(request):
    if request.method=='POST':
        form=FileForm(request.POST,request.FILES)
        fs=FileSystemStorage()
        print(request.FILES)
        print("asdaisdfiasvd")
        #form.url=fs.url(request.POST.name)
        if form.is_valid:
            form.save()
            return redirect('main/')
    else :
        form=FileForm()
    return render(request,'main/upload.html',{'form':form})
def home(request):
    return render(request, 'main/home.html',{'files':File.objects.all()})
class User(LoginView):
    template_name="main/login.html"
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('main/')
        else:
            return HttpResponseRedirect('login')