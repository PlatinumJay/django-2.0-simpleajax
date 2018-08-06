# django-2.0-simpleajax

## General
A simple app for Django 2.0+ with a form that sends back the input data on button click via AJAX.

## Structure

```sh
..
 |-- home
        |-- views.py
        |-- urls.py
 |-- templates
         |-- home
                |-- index.html
```

## Usage

Create the app for your project. In this example the app is named Home. Update your main settings.py to include the home app:

```sh
settings.py

...
INSTALLED_APPS = [
  ...
  'home.apps.HomeConfig',
]
```

Update the project urls.py file to add the Home app. Add the import include as well.

```sh
urls.py

...

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
]
```

