from django.urls import path
from .views import home, vending_machine, add_vending_machine, edit_vending_machine, remove_vending_machine, add_item, edit_item, remove_item, purchase

urlpatterns = [
    path('', home, name='home'),
    path('vending_machine/<int:id>/', vending_machine, name='vending_machine'),
    path('add/', add_vending_machine, name='add_vending_machine'),
    path('edit/<int:id>/', edit_vending_machine, name='edit_vending_machine'),
    path('remove/<int:id>/', remove_vending_machine, name='remove_vending_machine'),
    path('addItem/<int:id>/', add_item, name='add_item'),
    path('editItem/<int:id>/', edit_item, name='edit_item'),
    path('removeItem/<int:id>/', remove_item, name='remove_item'),
    path('purchase/<int:id>/', purchase, name='purchase'),
]