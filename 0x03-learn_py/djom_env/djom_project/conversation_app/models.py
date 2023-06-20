from django.db import models
from django.contrib.auth.models import User
from item_app.models import Item


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-modified_at',)
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'

    def __str__(self) -> str:
        return f"conversation: {self.members}"
    

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)


    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'ConversationMessage'
        verbose_name_plural = 'ConversationMessages'

    def __str__(self) -> str:
        return f"conversation message: {self.conversation}"