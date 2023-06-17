from django.shortcuts import render, redirect
from item_app.models import Category, Item
from .forms import SignUpForm

def index(req):
    items = Item.objects.filter(is_sold=False)[0:20]
    categories = Category.objects.all()
    return render(request=req, template_name='main/index.html', context={
        'items': items,
        "categories": categories,
    })

def contact(req):
    return render(request=req, template_name='main/contact.html', context={})

def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else: 
        form = SignUpForm()
    return render(request=req, template_name='main/signup.html', context={
        'form': form
    })
