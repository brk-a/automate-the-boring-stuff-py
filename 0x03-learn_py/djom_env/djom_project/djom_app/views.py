from django.shortcuts import render

def index(req):
    return render(request=req, template_name='main/index.html', context={})

def contact(req):
    return render(request=req, template_name='main/contact.html', context={})
