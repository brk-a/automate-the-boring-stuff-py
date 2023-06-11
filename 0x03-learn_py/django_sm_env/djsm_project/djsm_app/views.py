from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(request=req, template_name='main/index.html')
