from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .forms import RegisterUserForm
from .models import User

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist.!!!")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email Or Password is invalid.!!!")
    context = {'page': 'login', 'form_title': "SignIn"}
    return render(request, "users/register_login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegisterUserForm()
    context = {"form": form, 'form_title': "Registration"}
    return render(request, "users/register_login.html", context)

    


