from django.urls import path,include
from. views import  *

urlpatterns = [
    path('vendor/<slug:slugquery>',vendor_home,name='vendor'),

]