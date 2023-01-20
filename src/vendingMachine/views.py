from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from .models import VendingMachine, Item
from django.core import serializers


# Create your views here.
def home(request):
    vending_machines = VendingMachine.objects.all()
    json_data = serializers.serialize('json', vending_machines)
    return JsonResponse(json_data, safe=False)


def vending_machine_list(request):
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
            'items': items_list
        })
    return JsonResponse(vending_machines_list, safe=False)


def vending_machine_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')

        if name and location:
            vending_machine = VendingMachine.objects.create(name=name, location=location)
            return JsonResponse({
                'name': vending_machine.name,
                'location': vending_machine.location,
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def vending_machine_edit(request, vending_machine_id):
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


def vending_machine_remove(request, vending_machine_id):
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    if request.method == "POST":
        vending_machine.delete()
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest()


def item_create(request, vending_machine_id):
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
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


def item_edit(request, vending_machine_id, item_id):
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
        item = Item.objects.get(id=item_id, vending_machine=vending_machine)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
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
                'vending_machine': item.vending_machine.location
            })
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def item_remove(request, vending_machine_id, item_id):
    try:
        vending_machine = VendingMachine.objects.get(id=vending_machine_id)
        item = Item.objects.get(id=item_id, vending_machine=vending_machine)
    except VendingMachine.DoesNotExist:
        raise Http404("Vending machine does not exist")
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
    if request.method == "POST":
        item.delete()
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest()
