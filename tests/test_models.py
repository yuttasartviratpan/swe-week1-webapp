from django.test import TestCase
from vendingMachine.models import VendingMachine, Item


class VendingMachineModelsTestCase(TestCase):
    def setUp(self):
        VendingMachine.objects.create(name="Machine 1", location="Bangkok")
        VendingMachine.objects.create(name="Machine 2", location="Chiang Mai")

    def test_vending_machine_entity(self):
        machine_no_1 = VendingMachine.objects.get(name="Machine 1")
        machine_no_2 = VendingMachine.objects.get(name="Machine 2")

        Item.objects.create(
            vending_machine=machine_no_1,
            name="Spaghetti",
            price="19.99",
            quantity="100",
        )
        Item.objects.create(
            vending_machine=machine_no_1, name="Apple", price="9.99", quantity="10"
        )
        Item.objects.create(
            vending_machine=machine_no_1,
            name="Mineral Water",
            price="2.99",
            quantity="1000",
        )

        self.assertEqual(str(machine_no_1), "Machine 1")
        self.assertEqual(str(machine_no_2), "Machine 2")
