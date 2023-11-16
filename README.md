## Getting Started

### Existing Django Apps

Check out existing Django apps at [Django Packages](https://djangopackages.org/categories/apps/) to discover and integrate additional functionality into your project.


### Create a package in Django (appone)

To create the "appone" package in your Django project, run the following command:

```bash
python manage.py startapp appone
```

## Contents of Django package (appone)

1. **apps.py:** Configuration file for the app within the project.

2. **views.py:** Handles HTTP responses for the browser.

3. **models.py:** Defines data models and tables. Synchronizes data in the database from the defined classes.

4. **admin.py:** Configuration file for the administration interface to manage models.

## Adding the application of the package to the Django project

Navigate to your project directory (e.g., "mywebproject") and open the `settings.py` file. Add the following line to the `INSTALLED_APPS` section:
"appone.apps.ApponeConfig"
```python
# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "appone.apps.ApponeConfig",
]
```
Without this line all models which we want to synchronize with the database will not be considerate by Django.
With this reference our project mywebproject recognize appone

Certainly! Here's the integration of the provided paragraph in French into your README.md in English:

## Routing

Routing in Django involves deciding which function will handle an incoming HTTP request and, consequently, be responsible for generating the response. In the context of Django, this is defined in the `urls.py` file.

In the `urls.py` file, a list of paths is associated with corresponding functions. This mapping determines the entry point for a request, helping to direct requests to the appropriate functions within the Django application.

Our request handling is divided into two parts:

1. The request processing part, located in the `appone` package's `views.py`. Here, we define the functions that will handle the requests.

   ```python
   from django.http import HttpResponse

   def hello(request):
       return HttpResponse('Hello Django! appone application')
   ```

2. The routing part, where we define the URL that should be called. This is done in the `mywebproject`'s `urls.py`, and we import the views from `appone` and add the path "hello/" with the associated `views.hello` function.

   ```python
   from appone import views

   urlpatterns = [
       path("admin/", admin.site.urls),
       path("hello/", views.hello),
   ]
   ```

## Launch the Web Server

To run the web server, execute the following command:

```bash
python manage.py runserver
```

Go to the browser and enter the following in the search bar to see the response:

[http://127.0.0.1:8000/hello/](http://127.0.0.1:8000/hello/)


## Routing Rules

Routing rules in Django involve defining matching rules for paths, 
providing arguments to Python functions, and organizing routes by application for better management.

Add the following view to your `apptwo` under `views.py`:

```python
# apptwo/views.py
from django.http import HttpResponse

def picture_detail(request,category, year=0, month=1 ):
   body = "Category={}, year = {}, month = {}".format(category, year, month )
   return HttpResponse(body)
```

In `urls.py`, add the following paths to the urlpatterns: 

```python
# mywebproject/urls.py
from appone import views
from apptwo import views as v2

urlpatterns = [
   path("admin/", admin.site.urls),
   path("hello/", views.hello),
   path("djangorocks/", v2.djangorocks),
   path("picture/<str:category>/", v2.picture_detail),
   path("picture/<str:category>/<int:year>/", v2.picture_detail),
   path("picture/<str:category>/<int:year>/<int:month>/", v2.picture_detail)
]
```

Now, go to the browser and enter the following in the search bar to see the response:

- [http://127.0.0.1:8000/picture/landscape/](http://127.0.0.1:8000/picture/landscape/)
- [http://127.0.0.1:8000/picture/landscape/2023](http://127.0.0.1:8000/picture/landscape//2023/)
- [http://127.0.0.1:8000/picture/landscape/2023/12](http://127.0.0.1:8000/picture/landscape/2023/12/)


### Create Our Own Rule

In this paragraph, we aim to create a routing rule that allows entering the day of the month in only 2 digits. Follow these steps:

1. Create `converters.py` under `apptwo`.
2. Put the following code inside the file:

    ```python
    # apptwo/converters.py
    class TwoDigitDayConverter:
        regex = '[0-9]{2}'

        def to_python(self, value):
            return int(value)

        def to_url(self, value):
            return '%02d' % value
    ```

3. Update `views.py` as follows:

    ```python
    # apptwo/views.py
    def picture_detail(request, category, year=0, month=0, day=0):
        body = "Category={}, year={}, month={}, day={}".format(category, year, month, day)
        return HttpResponse(body)
    ```

4. Update `urls.py` as follows:

    ```python
    # mywebproject/urls.py
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("hello/", views.hello),
        path("djangorocks/", v2.djangorocks),
        path("picture/<str:category>/", v2.picture_detail),
        path("picture/<str:category>/<int:year>/", v2.picture_detail),
        path("picture/<str:category>/<int:year>/<int:month>/", v2.picture_detail),
        path("picture/<str:category>/<int:year>/<int:month>/<dd:day>/", v2.picture_detail),
    ]
    ```

Check the sound:

[http://127.0.0.1:8000/picture/landscape/2023/12/01](http://127.0.0.1:8000/picture/landscape/2023/12/01)

If we want to ensure that the provided format of the day is larger than 2 digits, an error will occur. Try this:

[http://127.0.0.1:8000/picture/landscape/2023/12/001](http://127.0.0.1:8000/picture/landscape/2023/12/001)


### Routing Each App

For better organization, we can separate the URLs of each application. Create a file `urls.py` under `apptwo`. This file will contain only the things related to `apptwo`.

```python
# apptwo/urls.py
from django.urls import path
from django.urls import register_converter

from apptwo import views as v2
from apptwo import converters

register_converter(converters.TwoDigitDayConverter, 'dd')

urlpatterns = [
    path("djangorocks/", v2.djangorocks),
    path("pictures/<str:category>/", v2.picture_detail),
    path("pictures/<str:category>/<int:year>/", v2.picture_detail),
    path("pictures/<str:category>/<int:year>/<int:month>/", v2.picture_detail),
    path("pictures/<str:category>/<int:year>/<int:month>/<dd:day>/", v2.picture_detail),
]
```

Then, return to `urls.py` under the project `mywebproject` and update it as follows:

```python
# mywebproject/urls.py
from django.contrib import admin
from django.urls import path, include
from appone import views

urlpatterns = [
   path("admin/", admin.site.urls),
   path("hello/", views.hello),
   path("apptwo/", include("apptwo.urls"))
]
```
We need now to add apptwo in our url in the browser like this: 
[http://127.0.0.1:8000/apptwo/pictures/landscape/2023/12/01](http://127.0.0.1:8000/apptwo/picture/landscape/2023/12/01)
This structure allows each app to manage its own URLs independently, providing a cleaner and more modular organization for your Django project.

# Discover the Django Template

- Model for generating HTML.
- DTL (Django Template Language) -> Format variables & Reuse blocks.

To create templates in Django, it happens in two parts:
1. Template file part: It can be HTML or anything else where we write HTML code, along with DTL code to inject our Python variables.
2. Injection part: Done on the views side (in the Django application).

To ensure that a template is visible and configurable by Django, you need to check the configuration. In `mywebproject -> settings.py`, here is the template configuration for our Django project:

```python
TEMPLATES = [
   {
      "BACKEND": "django.template.backends.django.DjangoTemplates",
      "DIRS": [],
      "APP_DIRS": True,
      "OPTIONS": {
         "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
         ],
      },
   },
]
```

- `"DIRS": []`: It is the list where Django will look for our template files to load. By default, it is an empty list because Django will look for all folders named `templates` by default.
- `"APP_DIRS": True`: With the value True, it means that Django will look for the `templates` folder inside our apps. It is recommended to separate templates by application to make them more independent.

## Create Our First Template

1. Go to the `apptwo` folder and create a new folder named `templates`.
2. Inside the new `templates` folder, create a folder with the same name as your application, in our case, `apptwo`.
3. Inside `apptwo\templates\apptwo`, create an HTML file named `index.html`.

Inside the `index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Index AppTwo</title>
</head>
<body>
<h1>This is AppTwo</h1>

<div style="background: #ff0000;">Lorem ipsum text</div>

</body>
</html>
```

4. Go to `views.py` and modify it as follows:

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def djangorocks(request):
   return HttpResponse('This is a Jazzy Response')

def picture_detail(request, category, year=0, month=0, day=0):
   template = loader.get_template('apptwo/index.html')
   return HttpResponse(template.render({}, request))
```

This structure demonstrates how to create and integrate templates into your Django project, allowing for dynamic HTML generation.
To see the change go to : 
[http://127.0.0.1:8000/apptwo/pictures/portrait](http://127.0.0.1:8000/apptwo/pictures/portrait)