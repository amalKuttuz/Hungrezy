from django.shortcuts import render
from.models import *
# Create your views here.
def vendor_home(request,slugquery):
    products=Products.objects.filter()
    return render(request,'vendor/home.html',{'products':products})