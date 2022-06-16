# DJANGO REST FRAMEWORK CRUD


### DESCRIPTION:

- CRUD application built with Django Rest Framework.

### INSTALLATION:

From project root:
```bash
virtualenv django-rest-env

source django-env/bin/activate

pip install -r requirements.txt

python manage.py runserver

```


### TESTS:

```bash
python manage.py test
```


### ENDPOINTS AIRCRAFT:

- #### GET `/api/aircraft/<serial_number>/`

  List aircraft by the `serial_number` provided.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/aircraft/api/2/
  ```

- #### PUT `/api/aircraft/<serial_number>/`

  Method to modify an item in the database.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/aircraft/api/2/ -d '{"manufacturer": "new_manufacturer"}'
  ```

- #### DELETE `/api/aircraft/<serial_number>/`

  Delete the item of the database with the `serial_number`.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/aircraft/2/


- #### GET `/api/aircraft/`

  List all items of the table.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/aircraft/

  ```

- #### POST `/api/aircraft/`

  Method to create an aircraft in the database.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/aircraft/ -d '{"serial_number": "1", "manufacturer": "manufacturer_1"}'
  ```


---

### ENDPOINTS FLIGHT:

- #### GET `/api/flight/<flight_id>/`

  List flight by the `flight_id` provided.

  Example:
  ```bash
  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/flight/14ca0657-c9db-4ee1-864a-144ed385550a/
  ```

- #### PUT `/api/flight/<flight_id>/`

  Method to the `arrival_timestamp` and/or the aircraft related to a flight in the database.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X PUT http://127.0.0.1:8000/api/flight/2c0fe678-0d07-43e5-a6cd-c1ae70b0f029/ -d '{"arrival_timestamp": "2022-06-15T21:10:36.091024Z", "aircraft_serial_number": 12323121}'
  ```


- #### DELETE `/api/flight/<flight_id>/`

  Delete the item of the database with the `flight_id`.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/flight/14ca0657-c9db-4ee1-864a-144ed385550a/
  ```


- #### GET `/api/flight/`

  List all items of the table.

**Querystrings parameters**:
- departure_airport
- arrival_airport
- start_time
- end_time

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/flight/?departure_airport=dep_airport_1&arrival_airport=%22arrival_airport_1%22&start_time=2022-06-15T20:08:36.091024Z&end_time=2022-06-15T20:13:36.091024Z

  ```

- #### POST `/api/flight/`

  Method to create a flight in the database. It is possible to assign a existing aircraft to a flight in this method.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/flight/ -d '{"departure_airport": "dep_airport_3", "departure_timestamp": "2022-06-16T21:10:36.091024Z", "arrival_airport": "arrival_airport_3", "aircraft_serial_number": 12323121}'
  ```
