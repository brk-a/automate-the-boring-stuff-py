from django.shortcuts import get_object_or_404, redirect, render
from .models import Conversation
from . forms import ConversationMessageForm
from item_app.models import Item

def new_conversation(req, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == req.user:
        return redirect('dashboard_app:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[req.user.id])
    if conversations:
        pass #redirect to existing convo

    if req.method == 'POST':
        form = ConversationMessageForm(req.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(req.user)
            conversation.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = req.user
            conversation_message.save()

            return redirect('item_app:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request=req, template_name='conversations/new.html', context={
        'form': form,
    })
