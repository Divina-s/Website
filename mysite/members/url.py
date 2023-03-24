from django.urls import path
from .views import UserEditView, registerView, login_userView, logout_userView

urlpatterns = [
    path('register/', registerView, name ='register'),
    path('login', login_userView, name='login'),
    path('logout',logout_userView, name='logout'),
    path('edit_profile', UserEditView, name='edit-profile' )


]
