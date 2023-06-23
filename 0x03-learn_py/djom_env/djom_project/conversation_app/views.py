from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Conversation
from . forms import ConversationMessageForm
from item_app.models import Item

@login_required
def new_conversation(req, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == req.user:
        return redirect('dashboard_app:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[req.user.id])
    if conversations:
        return redirect('conversation_app:detail', pk=conversations.first().id)

    if req.method == 'POST':
        form = ConversationMessageForm(req.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(req.user)
            conversation.members.add(item.created_by)
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

@login_required
def inbox(req):
    conversations = Conversation.objects.filter(members__in=[req.user.id])

    return render(request=req, template_name='conversations/inbox.html', context={
        'conversations' : conversations,
    })

@login_required
def detail(req, pk): #conversation pk, not item pk
    conversation = Conversation.objects.filter(members__in=[req.user.id]).get(pk=pk)

    if req.method == 'POST':
        form = ConversationMessageForm(req.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = req.user
            conversation_message.save()

            conversation.save()
            # messages.success(req,'Your message has been sent!')
            return redirect('conversation_app:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request=req, template_name='conversations/detail.html', context={
        'conversation' : conversation,
        'form': form,
    })