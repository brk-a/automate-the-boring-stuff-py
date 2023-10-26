from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerialiser(ModelSerializer):
    """serialiser for model Note"""
    class Meta:
        model = Note
        fields = '__all__'