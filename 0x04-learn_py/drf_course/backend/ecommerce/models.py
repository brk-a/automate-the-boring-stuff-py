from django.db import models
from django.contrib.auth.models import User
from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
)


class Item(
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
    Model,
):
    """
    ecommerce.Item
    stores a single item entry for the shop
    """


    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title
    
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    def amount(self):
        #converts price from Kenyan cents to KES
        amount = float(self.price/100)
        return amount
    
    def manage_stock(self, qnty):
        #use this to reduce the qnty of an item of stock
        new_stock = self.stock - int(qnty)
        self.stock = new_stock
        self.save()

    def check_stock(self, qnty):
        #check if order qnty exceeds stock levels
        if int(qnty) > self.stock:
            return False
        return True
    
    def place_order(self, user, qnty):
        #place an order
        if self.check_stock(qnty):
            order = Order.objects.create(
                item=self,
                quantity=qnty,
                user=user
            )
            self.manage_stock(qnty)
            return order


class Order(
    TimeStampedModel,
    ActivatorModel,
    Model,
):
    """
    ecommerce.Order
    stores a single order entry related to :model: `ecommerce.Item`
    and :model: `auth.User`
    """

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = 'Orders'
        ordering = ["id"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.item.title}'
