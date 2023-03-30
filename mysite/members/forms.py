from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email',)

class ProfilePageForm(forms.ModelForm):
     class Meta:
      model=Profile
      fields=('bio','profile_pic','Github_url','facebook_url','twitter_url','linkedIn_url')
      widgets={
         
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            #'profile_poc': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user','type':'hidden'}),
            'Github_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedIn_url': forms.TextInput(attrs={'class':'form-control'}),

        }
     