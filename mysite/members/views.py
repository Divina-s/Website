from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView



def registerView(request, *args, **kwargs):
    if request.method =="POST":
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        user_name =request.POST['username']
        password =request.POST['pass']

        new_user=User.objects.create_user(username=user_name, email=email, password=password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        return redirect('login')
    return render(request, 'register.html', {})
@login_required
def home(request):
    return render(request, 'home.html',{})
def login_userView(request):
    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        User=authenticate(request,username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            return HttpResponse('Error, User does not exist')       
    else:         
       return render(request, 'login.html', {})
    
def logout_userView(request):
    logout(request)
    return redirect('home')

# Create your views here.
def UserEditView(generic,CreateView):
    form_class=UserChangeForm
    template_name='edit_profile.html'
    success_url=reverse_lazy('home')