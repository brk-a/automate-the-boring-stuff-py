# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .models import Note
# from .serialisers import NoteSerialiser
from .utils import updateNote, deleteNote, getOneNote, getAllNotes, createNote

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)
    # return JsonResponse(f"This API returns {routes}", safe=False)

@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method=='GET':
        return getAllNotes(request)
    if request.method=='POST':
        return createNote(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method=='GET':
        return getOneNote(request, pk)
    if request.method=='PUT':
        return updateNote(request, pk)
    if request.method=='DELETE':
        return deleteNote(request, pk)
