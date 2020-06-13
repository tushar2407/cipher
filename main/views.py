from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  FileForm, SignUpForm
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
@login_required
def home(request):
    return render(request, 'main/home.html',{'files':File.objects.filter(user=request.user)})
class UserLogin(LoginView):
    template_name="main/login.html"
    """def get(self, request):
        if request.user.is_authenticated:
            return redirect('/main')"""
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/main')
        else:
            return HttpResponse(content="not authorised")
class UploadFile(LoginRequiredMixin,CreateView):
    login_url='/main/login'
    template_name='main/upload.html'
    form_class=FileForm
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    """def form_save(self,form):
        fs=FileSystemStorage()
        if not fs.exists(form.instance.name):
            fs.save(form.instance.name, form.instance.file)
        return super().form_save(form)        """
def signup(request):
    context={}
    if request.method=='POST':
        form=SignUpForm(request.POST)
        """temp=User.objects.get(user=request.POST['username'])
        if temp:
            Profile.objects.create(user=request.POST)"""
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.birth_date=form.cleaned_data.get('birth_date')
            print(user.profile.birth_date)
            user.save()
            user=authenticate(request,username=request.POST['username'],password=request.POST['password1'])
            login(request,user)
            return redirect('/main')
        else:
            #print(form.errors.as_json())
            context['errors']=form.errors
            #print(context['errors'][0])
            context['form']=SignUpForm()
            return render(request,'main/signup.html',context)
    form=SignUpForm()
    context['form']=form
    """if request.user.is_authenticated:
        return redirect('/main')"""
    return render(request, 'main/signup.html',context)
def delete(request, pk):
    File.objects.get(pk=pk).delete()
    return redirect('/main')
@login_required
def profile(request):
    context={}
    request.user.refresh_from_db()
    print(str(request.user.profile.birth_date))
    context['files']=File.objects.filter(user=request.user)
    context['profile']=request.user.profile
    context['birthDate']=str(request.user.profile.birth_date)
    return render(request,'main/profile.html', context)