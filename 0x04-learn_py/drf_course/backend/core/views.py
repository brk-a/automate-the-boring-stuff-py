from django.shortcuts import render
from json import JSONDecodeError
from django.http import JsonResponse
from .serialisers import ContactSerialiser
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response


class ContactAPIView(views.APIView):
    """
    a simple API view to create contact entries
    """
    serialiser_class = ContactSerialiser

    def get_serialiser_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serialiser(self, *args, **kwargs):
        kwargs['context'] = self.get_serialiser_context()
        return self.serialiser_class(*args, **kwargs)
    
    def post(self, req):
        try:
            data = JSONParser().parse(req).data
            serialiser = ContactSerialiser(data=data)

            if not serialiser.is_valid(raise_exception=True):
                serialiser.save()
                return Response(serialiser.data)
            else:
                return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

        except JSONDecodeError:
            return JSONDecodeError({
                "result": "error",
                "message": "JSON decode error"
            }, status=400)
