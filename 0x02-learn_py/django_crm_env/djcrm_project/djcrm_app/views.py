from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from . models import Record


def home(req):
    records = Record.objects.all()

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

    return render(request=req, template_name='main/home.html', context={'records': records})

# def login_user(req):
#     pass

def logout_user(req):
    logout(req)
    messages.success(req, f'Logout imefaulu. Kwaheri.')
    return redirect('home')

def register_user(req):
    if req.method == 'POST':
        form  = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user=user)
            messages.success(req, f'Karibu, {username.lower()}!')
            return redirect('home')
    else:
        form = SignUpForm() #not passing `req` because user has not filled form, yet
        return render(request=req, template_name='main/register.html', context={'form':form})
    
    return render(request=req, template_name='main/register.html', context={'form': form})

def customer_record(req, pk):
    if req.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request=req, template_name='record.html', context={'record': customer_record})
    else:
        messages.success(req, f'Haikufaulu. Log in kisha ujaribu tena.')
        return redirect('home')