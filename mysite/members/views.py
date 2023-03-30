from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,CreateView
from blog.models import Profile
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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
        messages.success(request,'Your account has been created!, Please LOGIN')
        return redirect('login')
    return render(request, 'register.html', {})


def login_userView(request):
    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        User=authenticate(request,username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            messages.error(request,'User does not exist!')
            return redirect('login')       
    else:         
       return render(request, 'login.html', {})
    
def logout_userView(request):
    logout(request)
    return redirect('home')

# Create your views here.
class ShowProfilePageView(DetailView):
    model= Profile
    template_name='user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users= Profile.objects.all()
        context=super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user=get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"]= page_user
        return context
    

class EditProfileView(UpdateView): 
    form_class=EditProfileForm
    template_name='edit_profile.html'
    success_url=reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
class PasswordsChangeView(SuccessMessageMixin,PasswordChangeView):
    """ Success"""
    form_class=PasswordChangeForm 
    template_name='change_password.html' 
    success_message= 'Your Password has been changed successfully!'
    success_url=reverse_lazy('home')

def password_success(request):
    messages.success(request, 'Your Password has been changed successfully!')
    return render(request,'home.html')    
class EditProfilePageView(generic.UpdateView):
    model=Profile
    form_class=ProfilePageForm
    template_name="edit_profile_page.html"
    success_url=reverse_lazy('home')
#fields=[ 'bio','profile_pic','Github_url','facebook_url', 'twitter_url', 'linkedIn_url']
class CreateProfilePageView(SuccessMessageMixin,CreateView):
    model=Profile
    template_name='create_profile.html'
    success_url=reverse_lazy('home')
    success_message='Your Profile has been created!!!'
    form_class= ProfilePageForm


    def form_valid(self, form):
      form.instance.user=self.request.user
      return super().form_valid(form)

    