from django.urls import path,include
from. views import  *

urlpatterns = [
    path('signin',signin.as_view(), name='signin'),
    path('signup',signup.as_view(), name='signup')


]