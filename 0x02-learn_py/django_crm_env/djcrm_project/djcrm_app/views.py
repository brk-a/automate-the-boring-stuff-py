from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user=user)
            messages.success(req, f'Karibu, {username.lower()}!')
            return redirect('home')
        else:
            messages.success(req, f'Login haikufaulu. Tafadhali jaribu tena.')
            return redirect('home')

    return render(request=req, template_name='main/home.html', context={})

# def login_user(req):
#     pass

def logout_user(req):
    logout(req)
    messages.success(req, f'Logout imefaulu. Kwaheri.')
    return redirect('home')

def register_user(req):
    return render(request=req, template_name='main/register.html', context={})