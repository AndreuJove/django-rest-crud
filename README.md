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
  curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/aircraft/api/2/


- #### GET `/api/aircraft/`

  List all items of the table.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/aircraft/api/

  ```

- #### POST `/api/aircraft/`

  Method to create an aircraft in the database.

  Example:

  ```bash
  curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/aircraft/api/ -d '{"serial_number": "1", "manufacturer": "manufacturer_1"}'
  ```
