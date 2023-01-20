from django import forms
from .models import VendingMachine, Item


class VendingMachineForm(forms.ModelForm):
    class Meta:
        model = VendingMachine
        fields = ['name', 'location']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'quantity']
