from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class VendingMachine(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    # Mapping item object to vending machine object. Many-to-one relationship
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    # time_stamp = models.ForeignKey(Time, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Time(models.Model):
    container = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    key = models.DateTimeField(default=timezone.localtime)  # date time
    # items = models.ManyToManyField(Item)
    items = models.JSONField(null=True)

    def __str__(self):
        return self.key