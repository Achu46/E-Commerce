from django.shortcuts import render
from.models import*
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

# # Create your views here.

# Sigup page
def create(request):
    if request.method == 'POST':
        Firstname = request.POST.get("Firstname")
        Lastname = request.POST.get("Lastname")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        ConfirmPassword = request.POST.get("ConfirmPassword")
        DOB = request.POST.get("DOB")
        Gender = request.POST.get("gender")

        if not all([Firstname, Lastname, Email, Password, ConfirmPassword, DOB, Gender]):
            return HttpResponseBadRequest("All fields are required.")

        if Password != ConfirmPassword:
            return HttpResponseBadRequest("Passwords do not match.")

        rowvalue = users.objects.create(
            Firstname=Firstname,
            Lastname=Lastname,
            Email=Email,
            Password=Password,
            DOB=DOB,
            Gender=Gender
        )
        rowvalue.save()
        return HttpResponse("Welcome, Successfully Registered")

    return HttpResponseBadRequest("Invalid request method.")

def signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,"signin.html")

# Sign in
def submit(request):
    Username=request.POST.get("username",False)
    Password=request.POST.get("password",False)
    if(Username!=False and Password!=False):
        rowvalue=users.objects.get(Firstname=Username,Password=Password)
        if rowvalue!=None:
            return HttpResponse("Welcome Back!")
        else:
            return HttpResponse("Sorry We can't find your Account")
    return HttpResponse("error")
    
def index(request):
    return render(request,'index.html')
def mens(request):
    return render(request,"mens.html")

def index(request):
    return render(request,'index.html')
def womens(request):
    return render(request,"womens.html")

def index(request):
    return render(request,'index.html')
def kids(request):
    return render(request,"kids.html")
