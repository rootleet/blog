from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .extras import is_email
from django.contrib.auth import authenticate, login as auth_login



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'account/login.html', context={'title': 'LOGIN'})


def login_process(request):
    # check request method
    method = request.method

    if request.method == 'POST':
        # method is valid
        form = request.POST

        # get form values
        ini = form['ini']
        key = form['key']

        # check if ini is email or username
        ini_split = ini.split('@')

        if is_email(ini):
            # email
            check_w = 'email'
            user_exist = User.objects.filter(email=ini)
        else:
            # username
            check_w = 'username'
            user_exist = User.objects.filter(username=ini)

        # check if user exist
        if user_exist.count() == 1:
            # there is user
            if check_w == 'email':
                us = User.objects.get(email=ini)
            else:
                us = User.objects.get(username=ini)

            # authenticate
            username = us.username
            auth = authenticate(request, username=username, password=key)

            # validate login with try and catch
            try:
                if hasattr(auth, 'is_active'):
                    auth_login(request, auth)
                    return redirect('home')
                else:
                    messages.error(request,f'Invalid Password {key} for user {username}')
            except Exception as e:
                messages.error(request, str(e))


        else:
            # there is no user
            messages.error(request, f"There is no account with {check} as {ini}")

    else:
        messages.error(request, "INVALID REQUEST METHOD")

    # return to login
    return redirect('login')



# register account
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'account/register.html',context={'title':'SIGN UP'})

def signup_process(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # validate form
        method = request.method
        if method == 'POST':
            form = request.POST
            username = form.get('username')
            email = form.get('email')
            password = form.get('password')

            try:
                # create account
                user = User.objects.create_user(username=username, email=email, password=password,is_staff=1,is_active=1)
                user.save()
                messages.success(request, "Please login")
                return redirect('login')
            except Exception as e:
                messages.error(request,str(e))
                return redirect('sign-up')

        else:
            messages.error(request,"INVALID REQUEST METHOD")

        redirect('sign-up')