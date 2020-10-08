# lone-django-orm
A small project to use django orm without rest of the django system. Made by following [james stewart's blog](https://jystewart.net/2008/02/18/using-the-django-orm-as-a-standalone-component/)

## Setup:
- Install requirements using `pip install -r requirements.txt`.
- Add present working directory to python path.
- export django setting file via `export DJANGO_SETTINGS_MODULE=settings` command.
- Make and run migrations using `django-admin makemigrations <app_name> && django-admin migrate` (project has orm as directory use same pattern to add more apps).
