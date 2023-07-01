from django.shortcuts import render
from json import JSONDecodeError
from django.http import JsonResponse
from .serialisers import ItemSerialiser, OrderSerialiser
from .models import Item, Order
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin


class ItemViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    simple viewset for listing or retrieving items
    """
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerialiser


class OrderViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    simple viewset to list, retrieve or create orders
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerialiser

    def get_queryset(self):
        """
        returns a list of orders for the user currently authenticated
        """
        user = self.request.user
        return Order.objects.filter(user=user)
    
    def create(self, req):
        try:
            data = JSONParser().parse(req)
            serialiser = OrderSerialiser(data=data)
            if serialiser.is_valid(raise_exception=True):
                item = Item.objects.get(pk=data["item"])
                order = item.place_order(req.user, data["quantity"])
                return Response(OrderSerialiser(order).data)
            else:
                return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "JSON decoding error"}, status=400)
