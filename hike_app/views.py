from django.shortcuts import render, redirect
from .models import Hike
from django.apps import apps
User = apps.get_model('login_app', 'User')
from django.contrib import messages

def dashboard(request):
    if 'user_id' in request.session:
        context={
            "hikes": Hike.objects.all(),
            "user": User.objects.get(id=request.session['user_id']),
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')
    return render(request, "dashboard.html")

def remove(request, hike_id):
    current_hike = Hike.objects.get(id=hike_id)
    current_user = User.objects.get(id=request.session['user_id'])
    current_hike.attend.remove(current_user)
    return redirect("/hikes")

def new(request):
    if request.method == "GET":
        return render(request, "add.html")
    else:
        errors = Hike.objects.hike_validation(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect("/hikes/new")
        else:
            logged_user = User.objects.get(id=request.session['user_id'])
            new_hike = Hike.objects.create(event_name=request.POST['event_name'], location=request.POST['location'], description=request.POST['description'], distance=request.POST['distance'], max_attendees=request.POST['max_attendees'], difficulty=request.POST['difficulty'], pets=request.POST['pets'], date=request.POST['date'], time=request.POST['time'], user=logged_user) 
            return redirect("/hikes/join")

def join(request):
    if request.method == "GET":
        context={
            "hikes": Hike.objects.all(),
            "user": User.objects.get(id=request.session['user_id']),
        }
        return render(request, "join.html", context)
def joinHike(request, hike_id):
    current_hike = Hike.objects.get(id=hike_id)
    current_user = User.objects.get(id=request.session['user_id'])
    attendees = current_hike.attend.all()
    for one_attendee in attendees:
        if current_user.id == one_attendee.id or current_hike.attend.count() == current_hike.max_attendees:
            return redirect("/hikes/join")
    current_hike.attend.add(current_user)
    return redirect("/hikes/join")

def logout(request):
    request.session.flush()
    return redirect("/")

def delete(request, hike_id):
    current_hike = Hike.objects.get(id=hike_id)
    current_hike.delete()
    return redirect("/hikes/join")

def edit(request, hike_id):
    if request.method == "GET":
        context={
            "current_hike" : Hike.objects.get(id=hike_id),
        }
        return render(request, "edit.html", context)
    else:
        errors = Hike.objects.hike_validation(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect(f"/hikes/edit/{hike_id}")
        else:
            current_hike = Hike.objects.get(id=hike_id)
            current_hike.event_name = request.POST['event_name']
            current_hike.location = request.POST['location']
            current_hike.description = request.POST['description']
            current_hike.max_attendees = request.POST['max_attendees']
            current_hike.difficulty = request.POST['difficulty']
            current_hike.pets = request.POST['pets']
            current_hike.date = request.POST['date']
            current_hike.time = request.POST['time']
            current_hike.user = User.objects.get(id=request.session['user_id'])
            current_hike.save()
            return redirect("/hikes/join")
def details(request, hike_id):
    context={
        "current_hike" : Hike.objects.get(id=hike_id)
    }
    return render(request, "details.html", context)

def account(request):
    if request.method == "GET":
        context={
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "account.html", context)
    else:
        user = User.objects.get(id=request.session["user_id"])
        errors=User.objects.update_user(request.POST, user.email)
        
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect("/hikes/account")
        else:
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect("/hikes/account")

