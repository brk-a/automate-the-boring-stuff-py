from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item_app.models import Item

@login_required
def index(req):
    items = Item.objects.filter(created_by=req.user)
    return render(request=req, template_name='dashboard/index.html', context={
        'items': items,
    })
