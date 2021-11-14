from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import RegisterUser,SigninUser,CreateToDoList
from django.contrib.auth.models import User
from .models import ToDoList
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):

    if request.method == "POST":
        form = CreateToDoList(request.POST)
        if form.is_valid():
            user = request.user
            ToDoList_query = ToDoList.objects.filter(user = user)
            txt = form.cleaned_data["text"] 
            t = ToDoList(user = user,text=txt)
            t.save()
    else:
        form = CreateToDoList(request.POST)

    return render(request,"mysite/home.html",{"form":form})

def signin(request):
    if request.method == "POST":
        form = SigninUser(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            p1 = form.cleaned_data["pass1"]
            u = authenticate(username =un,password=p1)
            
            if u is not None: 
                login(request,u) 
                fname = u.first_name
                return redirect("home")
            else:
                return redirect("signin")
    else:
        form = SigninUser(request.POST)

    return render(request,"mysite/signin.html",{"form":form})

def register(request):

    if request.method == "POST":
        form = RegisterUser(request.POST)

        if form.is_valid():
            un = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            e = form.cleaned_data["email"]
            p1 = form.cleaned_data["pass1"]
            p2 = form.cleaned_data["pass2"]
            u = User.objects.create_user(un,e,p1)
            u.first_name = fname
            u.lastname = lname
            u.save()

            return redirect("signin")
    else:
        form = RegisterUser(request.POST)

    return render(request,"mysite/register.html",{"form":form}) 


def signout(request):
    logout(request)
    return redirect("signin")

def viewitems(request):
    user = request.user
    ToDoList_query = ToDoList.objects.filter(user = user)

    return render(request,"mysite/viewitems.html",{"ToDoList_query" : ToDoList_query})