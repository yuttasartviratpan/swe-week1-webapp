# swe-week1-webapp

How to use: \
1. Go into src folder in terminal
2. type: "python manage.py runserver" (no quotes) in the terminal
3. Open your postman, set the url to "http://127.0.0.1:8000/"
4. Test stuff, try to send request. The available url are listed below:


Available urls:
1. "/" (root) - It returns all vending machine in the database in JSON
2. "/vending_machine/list/" - Returns detailed lists of vending machines, 
you will be able to see all the items in each of the vending machines
3. "/vending_machine/create/" - Take in POST request to create a new
vending machine. 2 fields should be specified, these being:
   1. name - name of the vending machine
   2. location - location of the vending machine
4. "/vending_machine/edit/[vending_machine_id]/" - Take in POST request to
edit the selected vending machine based on it's id. Vending machine's id can be
found by looking for it on (2.) JSON return. 2 fields should be specified, these being:
   1. name - name of the vending machine
   2. location - location of the vending machine
5.  "/vending_machine/remove/[vending_machine_id]/" - It removes the specified id 
of the vending machine. A JSON prompt should be seen based on whether
it succeeded or not
6. "/item/create/[vending_machine_id]/" - Take in POST request to add a items into a specified id of the
vending machine. 3 fields should be specified, these being:
   1. name - name of the item
   2. price - price of the item
   3. quantity - amount of the item in stock
7. "/item/edit/[vending_machine_id]/[item_id]/" - Take in POST request to edit the specified item id 
based on given vending machine id. Item id can be found on the (2.) JSON return. 
3 fields should be specified, these being:
   1. name - name of the item
   2. price - price of the item
   3. quantity - amount of the item in stock
8. "/item/remove/[vending_machine_id]/[item_id]/" - It removes the specified item id 
based on given vending machine id. A JSON prompt should be seen based on whether
it succeeded or not