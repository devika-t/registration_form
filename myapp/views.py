from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    myuser = User.objects.all()
    return render(request,'index.html',{})

def signup(request):

    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser=User.objects.create(email,password1)
        myuser.save()

        messages.success(request," Account created")
        return redirect('signin')
    return render(request,'signup.html')



def signin(request):

    if request.method == "POST":
        email=request.POST['email']
        password1=request.POST['password1']

        user=authenticate(email=email,password=password1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"/index.html",{'fname': fname})
        else:
            messages.error(request,"Error")
            return redirect('index')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('index')
