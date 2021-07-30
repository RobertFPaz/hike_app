from django.shortcuts import render, redirect
from . models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register_page(request):
    return render(request, 'register.html')

def register(request):
    if request.method == "POST":
        errors=User.objects.registration_validation(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect("/register_page")
        else:
            password=request.POST['password']
            pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['first_name']=new_user.first_name
            request.session['user_id']=new_user.id
            return redirect("/hikes")
    else:
        return redirect("/")
def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        errors=User.objects.login_validation(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect("/login_page")
        else:
            logged_user = User.objects.get(email=request.POST['email'])
            request.session['user_id']=logged_user.id
            request.session['first_name']=logged_user.first_name
            return redirect("/hikes")
    else: 
        return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")