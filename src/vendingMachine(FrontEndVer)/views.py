from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import VendingMachine, Item
from .forms import VendingMachineForm, ItemForm


# Create your views here.
def home(request):
    vending_machines = VendingMachine.objects.all()
    return render(request, 'home.html', {'vending_machines': vending_machines})


def vending_machine(request, id):
    vending_machine = VendingMachine.objects.get(id=id)
    items = Item.objects.filter(vending_machine=vending_machine)
    context = {'vending_machine': vending_machine, 'items': items}
    return render(request, 'vending_machine.html', context)


def add_vending_machine(request):
    if request.method == 'POST':
        form = VendingMachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VendingMachineForm()
    return render(request, 'add_vending_machine.html', {'form': form})


def edit_vending_machine(request, id):
    vending_machine = VendingMachine.objects.get(id=id)
    if request.method == 'POST':
        form = VendingMachineForm(request.POST, instance=vending_machine)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VendingMachineForm(instance=vending_machine)
    return render(request, 'edit_vending_machine.html', {'form': form})


def remove_vending_machine(request, id):
    vending_machine = VendingMachine.objects.get(id=id)
    vending_machine.delete()
    return redirect('home')


def add_item(request, id):
    vending_machine = VendingMachine.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.vending_machine = vending_machine
            item.save()
            return redirect('vending_machine', id=vending_machine.id)
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form, 'vending_machine': vending_machine})


def edit_item(request, id):
    item = Item.objects.get(id=id)
    vending_machine = item.vending_machine
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('vending_machine', id=vending_machine.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'vending_machine': vending_machine, 'item': item})


def remove_item(request, id):
    item = Item.objects.get(id=id)
    vending_machine = item.vending_machine
    item.delete()
    return redirect('vending_machine', id=vending_machine.id)



def purchase(request, id):
    item = Item.objects.get(id=id)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
        # record transaction
        return HttpResponse("Purchase Successful")
    else:
        return HttpResponse("Out of Stock")
