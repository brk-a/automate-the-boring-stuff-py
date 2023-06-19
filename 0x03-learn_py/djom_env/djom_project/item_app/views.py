from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item
from . forms import NewItemForm, EditItemForm

def items(req):
    query = req.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request=req, template_name='items/items.html', context={
        'items': items,
        'query': query,
    })

def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request=req, template_name='items/detail.html', context={
        'item': item,
        'related_items': related_items,
    })

@login_required
def new_item(req):
    if req.method == 'POST':
        form = NewItemForm(req.POST, req.FILES)
        if form.is_valid():
            item  = form.save(commit=False)
            item.created_by = req.user
            item.save()

            return redirect('item_app:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request=req, template_name='items/itemForm.html', context={
        'form': form,
        'title': 'Ongeza',
    })

@login_required
def delete_item(req, pk):
    try:
        item = get_object_or_404(Item, pk=pk, created_by=req.user)
    except Exception as e:
        print(f'deleteItemError: {e}')
        return
    else:
        item.delete()
    finally:
        redirect('dashboard_app:index')

@login_required
def edit_item(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    if req.method == 'POST':
        form = EditItemForm(req.POST, req.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_app:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request=req, template_name='items/itemForm.html', context={
        'form': form,
        'title': 'Hariri',
    })