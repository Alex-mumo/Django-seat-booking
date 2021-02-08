from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm #form for creating new users
from django.contrib.auth.models import User, auth #to handle user authentication
from django.contrib.auth import authenticate, login, logout #for loging in and logging out
from .forms import BusForm, CreateUserForm, StudentForm, BookingForm
from .models import Bus, Student, Booking, Contact #Bus , Student, Booking and Contact model
from django.http import HttpResponseRedirect , HttpResponse #using the HttpResponse
from django.contrib import messages #django system for sending messages
from django.contrib.auth.decorators import login_required  #user must be logged inc 
import datetime #importing the datetime model in python
from django.urls import reverse

@login_required(login_url = 'login')
def base(request): 
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

#@login_required(login_url =  'login') 
'''def bookbus(request):
    return render(request, 'bookbus.html')'''


@login_required(login_url = 'login')
def findbus(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): #check if the form is valid
            form.save()   #saves the form in the database
            messages.success(request, 'Booked Seat Successfully')
            return redirect("/findbus")  
    context = {'form': form}
    return render(request, 'findbus.html', context)
       
def LogOut(request):
    logout(request)
    redirect('login')
    return render(request, 'registration/logout.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): #checks if the form is valid
            form.save() #saves the form
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def about(request):
    context = {}
    return render(request, 'about.html')

def LogIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('base'))    
            else:
                return HttpResponse("Your account was active")
        else:
            print("someone tried to login and failed")
            print("They used used Username: {} and Password: {}.".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, "registration/login.html")
 
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        #creating contact instance
        obj = Contact(name = name, email = email, subject = subject, message = message)
        obj.save() #saves the instance
        messages.success(request , "Message sent successfully")
    return render(request, 'contact.html')

def show(request):
    buses_query = Bus.objects.all() #querying the all the database values 
    return render(request, 'show.html', {'buses_query': buses_query})



