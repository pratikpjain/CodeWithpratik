from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'home.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

def reset_password(request):
    return render(request,'reset_password.html')

def putQuestion(request):
    context = {
        "question" : "Find the even number"
    }
    return render(request, 'question.html', context)



