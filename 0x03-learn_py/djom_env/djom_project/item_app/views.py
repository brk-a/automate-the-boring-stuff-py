from django.shortcuts import get_object_or_404, render
from .models import Item

def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request=req, template_name='items/detail.html', context={
        'item': item,
    })