from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

# Create your views here.
class signup(View):
    def get(self,request):
        return render(request,'accounts/signup.html')
    def post(self,request):
        return redirect('signin')
    
class signin(View):
    def get(self,request):
        return render(request,'accounts/signin.html')
    def post(self,request):
        return redirect('home')