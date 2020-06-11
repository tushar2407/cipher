from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  FileForm
from .models import Profile, File
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
#from django.views.generic import TemplateView, LoginView
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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
