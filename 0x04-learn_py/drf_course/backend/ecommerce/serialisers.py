from collections import OrderedDict
from .models import Item, Order
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

class NotEnoughStockException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'There is not enough stock'
    default_code = 'invalid'


class ItemSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'title',
            'stock',
            'price',
        )


class OrderSerialiser(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset = Item.objects.all(), many=False)

    class Meta:
        model = Order
        fields = (
            'item',
            'quantity',
        )


    def validate(self, res: OrderedDict):
        """
        use this to validate stock level of Item
        """
        item = res.get("item")
        quantity = res.get("quantity")
        if not item.check_stock(quantity):
            raise NotEnoughStockException
        return res
