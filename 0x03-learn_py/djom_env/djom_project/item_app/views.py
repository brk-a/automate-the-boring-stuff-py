from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Item
from . forms import NewItemForm

def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request=req, template_name='items/detail.html', context={
        'item': item,
        'related_items': related_items,
    })

@login_required
def new_item(req):
    form = NewItemForm()

    return render(request=req, template_name='items/itemForm.html', context={
        'form': form,
        'title': 'New item',
    })