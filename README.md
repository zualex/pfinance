# Personal finance

## Run

- docker-compose up --build
- http://192.168.99.100:8000/


## DB

- docker exec -it pfinance_db_1 bash
- psql -p 5432 postgres postgres
- python manage.py migrate
- python manage.py makemigrations
- python manage.py sqlmigrate polls 0001
- python manage.py loaddata pfinance/fixtures/*

## Commands

- docker-compose up --build
- docker exec -it pfinance_web_1 bash
- python manage.py shell
- python manage.py test polls
- cp /usr/local/lib/python3.7/site-packages/django/contrib/admin/templates/admin/base_site.html /code/polls/templates

## Admin

- python manage.py createsuperuser


## Create a Django project

- docker-compose run web django-admin.py startproject pfinance
- python manage.py startapp wallets


## Style guide

- https://google.github.io/styleguide/pyguide.html
- https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/