from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User                      #to create user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app1.models import UserProfile
from django.forms.models import model_to_dict
import re
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


def user_signup(request):
    r = re.compile(r'[a-zA-Z]+') 
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pincode = request.POST.get("pincode")
        p1=make_password(password)
        confirmpass = request.POST.get("confirmpassword")
        profile_picture = request.POST.get("profile")
        address_line1 = request.POST.get("address_line1")
        city = request.POST.get("city")
        state =request.POST.get("state")
        try:
            if (password != confirmpass):
              return render(request, "user_signup.html", {"error1": True})
            else:
                 user = UserProfile(username=username, email=email, password=p1,
                        first_name=fname, last_name=lname, pincode=pincode,profile_picture=profile_picture,address_line1=address_line1,city=city,state=state)
                 user.save()
            return redirect("login")
        except Exception as e:
            print(e)
            return render(request, "user_signup.html", {"error2": True})
    return render(request, "user_signup.html")


def user_login(request):
    if request.method == 'POST':
        # global e
        user = request.POST.get("username")
        p = request.POST.get("password")
        print(user,p)
        users = UserProfile.objects.filter(username=user)
        print(users)
        if user is not None:
            user=users.first()
            request.session['username'] = user.username
            return redirect("dashboard")

        else:
            return render(request,"user_login.html",{"login" : True})
        
             
    return render(request,"user_login.html")


def dashboard(request):
    username = request.session.get('username')
    user = UserProfile.objects.get(username=username)
    return render(request, 'dashboard.html', {"data": user})


def logoutPage(request):
    logout(request)
    return redirect("login")