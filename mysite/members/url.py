from django.urls import path
from .views import  registerView,CreateProfilePageView ,login_userView, logout_userView, EditProfileView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('register/', registerView, name ='register'),
    
    path('login', login_userView, name='login'),
    path('logout',logout_userView, name='logout'),
    path('editprofile/',EditProfileView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='change_password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    
]
