from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import contact

# Create your views here.
def index(request):
    return render(request,"index.html")
def payment(request):
    return render(request,"payment.html")
def invoice(request):
    return render(request,"invoice.html")


def about(request):
    return render(request,"about.html")


def order(request):
    return render(request,"order.html")

def handlesignup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmpassword = request.POST.get('pass2')
        if (password != confirmpassword):
            messages.warning(request, "Password Is Incorrect.")
            return redirect('/signup')
        try:
            if User.objects.get(name=name):
                messages.info(request, "Username IS Taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request, "Email IS Taken")
                return redirect('/signup')
        except:
            pass

        myuser = User.objects.create_user(name, email, password)
        myuser.save()
        messages.success(request, "Sign Up Succesfully Please Login.")
        return render(request, "login.html")
    # return render(request,"signup.html")
    return render(request, "signup.html")

def handlelogin(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=name,password=pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Succesfully")
    return redirect('/login')

def handlecontact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        con=request.POST.get('comment')
        query=contact.objects.create(name=name,email=email,username=uname,desc=con)
        query.save()
        return render(request,"index.html")
    return render(request,"contact.html")