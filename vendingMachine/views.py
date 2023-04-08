from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponseBadRequest, Http404
from .models import VendingMachine, Item, Time
from django.core import serializers
from typing import Union
from django.utils import timezone
from copy import deepcopy
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime


def item_deep_copy(item):
    new_vending_machine = deepcopy(item.vending_machine)
    new_name = deepcopy(item.name)
    new_quantity = deepcopy(item.quantity)
    new_price = deepcopy(item.price)

    new_item = Item.objects.create(vending_machine=new_vending_machine, name=new_name, quantity=new_quantity,
                                   price=new_price)

    return new_item


# Create your views here.
def home(request: WSGIRequest) -> JsonResponse:
    """
    Root url. Return a brief list of vending machine in the database
    """
    vending_machines = VendingMachine.objects.all()
    json_data = serializers.serialize('json', vending_machines)
    return JsonResponse(json_data, safe=False)


def vending_machine_list(request: WSGIRequest) -> JsonResponse:
    """
    /vending_machine/list/
    Returns a detailed list of vending machine in the database
    This detailed list includes the product inside each vending machine
    """
    vending_machines = VendingMachine.objects.all()
    vending_machines_list = []
    for vending_machine in vending_machines:
        items = vending_machine.item_set.all()
        items_list = []
        for item in items:
            items_list.append({
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity
            })
        vending_machines_list.append({
            'id': vending_machine.id,
            'name': vending_machine.name,
            'location': vending_machine.location,
            'items': items_list,
        })
    return JsonResponse(vending_machines_list, safe=False)


def vending_machine_create(request: WSGIRequest) -> Union[JsonResponse, HttpResponseBadRequest]:
    """
    /vending_machine/create/
    Take in POST request to create vending machine.
    The fields must be input in a form of "form data"
    Return what you've inputted upon success, else BadRequestResponse
    """
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')

        if name and location:
            vending_machine = VendingMachine.objects.create(name=name, location=location)
            time_stamp = Time.objects.create(container=vending_machine, key=timezone.now())

            return JsonResponse({
                'name': vending_machine.name,
                'location': vending_machine.location
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def vending_machine_edit(request: WSGIRequest, vending_machine_id: int) -> Union[JsonResponse, HttpResponseBadRequest]:
    """
    vending_machine/edit/<vending_machine_id: int>/
    Take in POST request to edit vending machine.
    The vending machine id must be specified in the url
    The fields must be input in a form of "form data"
    Return what you've inputted upon success, else BadRequestResponse
    """
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')

        if name and location:
            vending_machine.name = name
            vending_machine.location = location
            vending_machine.save()
            return JsonResponse({
                'name': vending_machine.name,
                'location': vending_machine.location,
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def vending_machine_remove(request: WSGIRequest, vending_machine_id: int) -> Union[
    JsonResponse, HttpResponseBadRequest]:
    """
    vending_machine/remove/<int:vending_machine_id>/
    Take in POST request to remove vending machine.
    The vending machine id must be specified in the url
    No input in form data is necessary
    Return 'success' upon successful delete, else BadRequestResponse
    """
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    if request.method == "POST":
        vending_machine.delete()
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest()


def item_create(request: WSGIRequest, vending_machine_id: int) -> Union[JsonResponse, HttpResponseBadRequest]:
    """
    item/create/<int:vending_machine_id>/
    Take in POST request to create an item entity to a specific vending machine id.
    The vending machine id must be specified in the url
    The fields must be input in a form of "form data"
    Return what you've inputted upon success, else BadRequestResponse
    """
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    # time_stamp = Time.objects.create(container=vending_machine, key=timezone.now())
    time_stamp_item_list = []
    for item in vending_machine.item_set.all():
        # time_stamp.items.add(item_deep_copy(item))
        time_stamp_item_list.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'quantity': item.quantity
        })
    time_stamp = Time.objects.create(container=vending_machine, key=timezone.now(), items=time_stamp_item_list)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if name and price and quantity:
            item = Item.objects.create(name=name, price=price, quantity=quantity, vending_machine=vending_machine)

            return JsonResponse({
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity,
                'vending_machine': item.vending_machine.location
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def item_edit(request: WSGIRequest, vending_machine_id: int, item_id: int) -> Union[
    JsonResponse, HttpResponseBadRequest]:
    """
    item/edit/<int:vending_machine_id>/<int:item_id>/
    Take in POST request to create an item entity to a specific vending machine id.
    The vending machine id must be specified in the url
    The item id must be specified in the url
    The fields must be input in a form of "form data"
    Return what you've inputted upon success, else BadRequestResponse
    """
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
        item = Item.objects.get(id=item_id, vending_machine=vending_machine)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    # time_stamp = Time.objects.create(container=vending_machine, key=timezone.now())
    time_stamp_item_list = []
    for time_stamp_item in vending_machine.item_set.all():
        # time_stamp.items.add(item_deep_copy(item))
        time_stamp_item_list.append({
            'id': time_stamp_item.id,
            'name': time_stamp_item.name,
            'price': float(time_stamp_item.price),
            'quantity': time_stamp_item.quantity
        })
    time_stamp = Time.objects.create(container=vending_machine, key=timezone.now(), items=time_stamp_item_list)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if name and price and quantity:
            item.name = name
            item.price = price
            item.quantity = quantity
            item.save()
            return JsonResponse({
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity,
                'vending_machine': item.vending_machine.location,
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def item_remove(request: WSGIRequest, vending_machine_id: int, item_id: int) -> Union[
    JsonResponse, HttpResponseBadRequest]:
    """
    item/remove/<int:vending_machine_id>/<int:item_id>/
    Take in POST request to create an item entity to a specific vending machine id.
    The vending machine id must be specified in the url
    The item id must be specified in the url
    The fields must be input in a form of "form data"
    Return what you've inputted upon success, else BadRequestResponse
    """
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
        item = Item.objects.get(id=item_id, vending_machine=vending_machine)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    # time_stamp = Time.objects.create(container=vending_machine, key=timezone.now())
    time_stamp_item_list = []
    for time_stamp_item in vending_machine.item_set.all():
        # time_stamp.items.add(item_deep_copy(item))
        time_stamp_item_list.append({
            'id': time_stamp_item.id,
            'name': time_stamp_item.name,
            'price': float(time_stamp_item.price),
            'quantity': time_stamp_item.quantity
        })
    time_stamp = Time.objects.create(container=vending_machine, key=timezone.now(), items=time_stamp_item_list)
    if request.method == "POST":
        item.delete()
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest()


def check_item_timeline(request: WSGIRequest, vending_machine_id: int, item_id: int) -> Union[
    JsonResponse, Http404]:
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")

    date_list = []
    item_quantity = []
    time_stamp = vending_machine.time_set.all()
    for time in time_stamp:
        if not (time.items is None or len(time.items) == 0):
            for each_item in time.items:
                if item_id == each_item["id"]:
                    date_list.append(time.key)
                    item_quantity.append(each_item["quantity"])

    json_return_list = []
    for index in range(len(date_list)):
        json_return_list.append({
            'date': date_list[index],
            'quantity': item_quantity[index]
        })
    if len(json_return_list) == 0:
        raise Http404("Item does not exists.")
    else:
        return JsonResponse(json_return_list, safe=False)


def check_stock_timeline(request: WSGIRequest, vending_machine_id: int)-> Union[
    JsonResponse, Http404]:
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")

    time_stamp = vending_machine.time_set.all()
    time_stamp_list = []
    for time in time_stamp:
        time_stamp_list.append({
            'date': time.key,
            'items': time.items
        })

    return JsonResponse(time_stamp_list, safe=False)