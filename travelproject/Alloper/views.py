from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passwrd=request.POST['passw']
        user=auth.authenticate(username=username,password=passwrd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('/Alloper/login')
    return render(request,'login.html')
def register(request):
    if request.method =='POST':
        # name=request.POST["name"]
        username=request.POST["username"]
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        email=request.POST["emailid"]
        passwd=request.POST["passw"]
        cpass=request.POST["passwr"]
        if passwd==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('/Alloper/reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('/Alloper/reg')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=passwd)
                user.save();
                return redirect('/Alloper/login')
                print("create user")
        else:

            messages.info(request,"password not match")
            return redirect('/')

    return render(request,"reg.html")

def logout(request):
    auth.logout(request)
    return redirect('/')