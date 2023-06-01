from django.urls import path,include
from django.contrib.auth import views as auth_views

from. views import  *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('signup/',signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/',myaccount, name='myaccount'),



]