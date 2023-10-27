from rest_framework.response import Response

from .models import Note
from .serialisers import NoteSerialiser

def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serialiser = NoteSerialiser(note, many=False)
    return Response(serialiser.data)

def getAllNotes(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serialiser = NoteSerialiser(note, many=False)
    return Response(serialiser.data)

def getOneNote(request, pk):
    note = Note.objects.get(id=pk)
    serialiser = NoteSerialiser(note, many=False)
    return Response(serialiser.data)

def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serialiser = NoteSerialiser(instance=note, data=data)

    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note is deleted")