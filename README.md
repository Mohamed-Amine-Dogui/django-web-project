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
    path("picture/<str:category>/", v2.picture_detail),
    path("picture/<str:category>/<int:year>/", v2.picture_detail),
    path("picture/<str:category>/<int:year>/<int:month>/", v2.picture_detail),
    path("picture/<str:category>/<int:year>/<int:month>/<dd:day>/", v2.picture_detail),
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

This structure allows each app to manage its own URLs independently, providing a cleaner and more modular organization for your Django project.