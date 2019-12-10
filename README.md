## Django with PostgreSQL using Docker

#### A basic example of implementation of a api with Django using the Django Rest Framework library and Json web Token.

<p align="center">
  <img src="https://raw.githubusercontent.com/pydanny/pydanny.github.com/master/static/drf.png" width="350" height="190" />
</p>

Steps
---

##### Step 1: Clone repository:
    $ git clone https://github.com/vicabitu/basic-django-api-rest.git
    $ cd basic-django-api-rest

##### Step 2: Build the image:
    $ docker-compose build

##### Step 3: Once the image is built, run the containers:
    docker-compose up

##### Step 4: Run the migrations:
    docker-compose exec web python manage.py migrate --noinput


How to
---

##### Create super user:
    docker-compose exec web python manage.py createsuperuser

##### Stop containers:
    docker-compose stop