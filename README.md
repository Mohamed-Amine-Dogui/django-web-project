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

