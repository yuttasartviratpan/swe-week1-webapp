from django.urls import path
from .views import home, vending_machine_list, vending_machine_create, vending_machine_edit, vending_machine_remove, \
    item_create, item_edit, item_remove, check_item_timeline, check_stock_timeline

urlpatterns = [
    path('', home, name='home'),
    path('vending_machine/list/', vending_machine_list, name='vending_machine_list'),
    path('vending_machine/create/', vending_machine_create, name='vending_machine_create'),
    path('vending_machine/edit/<int:vending_machine_id>/', vending_machine_edit, name='vending_machine_edit'),
    path('vending_machine/remove/<int:vending_machine_id>/', vending_machine_remove,
         name='vending_machine_remove'),
    path('item/create/<int:vending_machine_id>/', item_create, name='item_create'),
    path('item/edit/<int:vending_machine_id>/<int:item_id>/', item_edit, name='item_edit'),
    path('item/remove/<int:vending_machine_id>/<int:item_id>/', item_remove, name='item_remove'),
    path('stock/product/<int:vending_machine_id>/<int:item_id>/', check_item_timeline, name='check_item_timeline'),
    path('stock/vending_machine/<int:vending_machine_id>/', check_stock_timeline, name='check_stock_timeline'),
]
