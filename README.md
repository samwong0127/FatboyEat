# Fatboy Eat API

# To run our application
1.  Run "docker-compose up" in folder: COMP3122-project
2.  Test by opening a new terminal and curling the endpoints e.g. "curl localhost:20080/menu/menus"


Here is all our API endpoints:
### Menu 
- Return a JSON object with all attributes of all menu sort by menu_id:
    - GET ``/menus`` 
- Return a JSON object with all the menus’ attributes of a store:
    - GET ``/stores/<store_id>/menus`` 
- Create or update the entire menu for a specific store:
    - POST ``/stores/<store_id>/menus`` 
- Updates an individual item within a menu:
    - POST ``/stores/<store_id>/menus/dishes/<dishes_id>``
- Delete an individual item within a menu:
    - DELETE ``/stores/<store_id>/menus/dishes/<dishes_id>``

### Order 
- Return a JSON object with all attributes of all orders:
    - GET ``/orders``
- Return a JSON object with all the orders’ attributes of a orderID:
    - GET ``/orders/<order_id>/list``
- Add an order for a specific store:
    - POST ``/addorder/stores/<storeID>``
- Delete an order for a specific store:
    - DELETE ``/deleteorder/orders/<OrderID>``

### Store 
- Return a JSON object with all attributes of all store sort by store_id:
    - GET ``/stores``
- Return a JSON object with all attributes of a specific store:
    - GET ``/stores/<store_id>``
- Return a JSON object with all attributes of a store with a specific category:
    - GET ``/stores/category/<categories>``

# To run tests
1.  Open a new terminal
2.  Type "cd FatboyEat"
3.  Type "pytest tests/unit.py"or "python3 -m pytest tests/unit.py"

# To visit Kibana
1.  Open a new browser.
2.  Visit localhost:5601
3.  Login using username ``elastic`` and password ``changeme``.

# To visit Prometheus
1.  Open a new browser.
2.  Visit localhost:9090

# To visit Grafana
1.  Open a new browser.
2.  Visit localhost:3000
3.  Login using username ``admin`` and password ``admin``.

# To visit Alertmanager
1.  Open a new browser.
2.  Visit localhost:9093