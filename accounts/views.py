from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from accounts.models import Userprofile
from django.contrib import messages  

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form
    })

def myaccount(request):
    
    return render(request,'accounts/myaccount.html')
