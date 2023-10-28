from rest_framework import serializers
from .models import Todo

class TodoSerialiser(serializers.ModelSerializer):
    """serialiser for to-do items"""
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')