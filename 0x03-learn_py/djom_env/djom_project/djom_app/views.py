from django.shortcuts import render
from item_app.models import Category, Item

def index(req):
    items = Item.objects.filter(is_sold=False)[0:20]
    categories = Category.objects.all()
    return render(request=req, template_name='main/index.html', context={
        'items': items,
        "categories": categories,
    })

def contact(req):
    return render(request=req, template_name='main/contact.html', context={})
