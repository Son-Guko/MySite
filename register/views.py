from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterFormLogin

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterFormLogin(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterFormLogin()
    return render(request, 'register/register.html', {'form':form})