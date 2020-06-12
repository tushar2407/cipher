from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  FileForm
from .models import Profile, File
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
"""@login_required
def upload(request):
    if request.method=='POST':
        #if request.user.is_authenticated:
        form=FileForm(request.POST,request.FILES)
        #fs=FileSystemStorage()
        if form.is_valid:
            form.save()
            return redirect('/main')
    else :
        form=FileForm()
        #print(form.as_p)
    return render(request,'main/upload.html',{'form':form})"""
def home(request):
    #print(File.objects.all())
    return render(request, 'main/home.html',{'files':File.objects.filter(user=request.user)})
class UserLogin(LoginView):
    template_name="main/login.html"
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/main')
        else:
            return HttpResponse(content="not authorised")
class UploadFile(CreateView):
    template_name='main/upload.html'
    form_class=FileForm
    success_url='/main'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    """def form_save(self,form):
        fs=FileSystemStorage()
        if not fs.exists(form.instance.name):
            fs.save(form.instance.name, form.instance.file)
        return super().form_save(form)        """