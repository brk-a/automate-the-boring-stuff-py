from django.shortcuts import render
from rest_framework import viewsets
from .serialisers import TodoSerialiser
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    """ to-do view """
    serializer_class = TodoSerialiser
    queryset = Todo.objects.all()
