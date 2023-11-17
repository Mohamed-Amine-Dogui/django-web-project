# Getting Started

### Create a Django project

To create a Django project called `mywebproject` inside the actual dir, run the following command: 

```bash
django-admin startproject mywebproject .
```

### Existing Django Apps

Check out existing Django apps at [Django Packages](https://djangopackages.org/categories/apps/) to discover and integrate additional functionality into your project.


### Create an application package in Django (appone)

To create the "appone" package in your Django project, run the following command:

```bash
python manage.py startapp appone
```

### Contents of Django package (appone)

1. **apps.py:** Configuration file for the app within the project.

2. **views.py:** Handles HTTP responses for the browser.

3. **models.py:** Defines data models and tables. Synchronizes data in the database from the defined classes.

4. **admin.py:** Configuration file for the administration interface to manage models.

### Adding the application package to the Django project

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

# Routing

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

## Launch the web server

To run the web server, execute the following command:

```bash
python manage.py runserver
```

Go to the browser and enter the following in the search bar to see the response:

[http://127.0.0.1:8000/hello/](http://127.0.0.1:8000/hello/)


## Routing rules

Routing rules in Django involve defining matching rules for paths, 
providing arguments to Python functions, and organizing routes by application for better management.

1. Create a second application package in Django:  run the following command:

```bash
python manage.py startapp apptwo
```

2. Add the following view to your `apptwo` under `views.py`:

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


### Create our own rule

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


### Routing each App

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

# Django template

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

## Create our first template

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


## Assign variables to a template

Go to `views.py` in `apptwo`, then modify the empty dictionary in the `picture_detail` function:

```python
def picture_detail(request, category, year=0, month=0, day=0):
   template = loader.get_template('apptwo/index.html')
   context = {
      'title': 'This is the picture detail'
   }
   return HttpResponse(template.render(context, request))
```

Then, modify our file `index.html` located under: `apptwo\templates\apptwo\index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Index AppTwo</title>
</head>
<body>
<h1>{{ title }}</h1>

<div style="background: #ff0000;">Lorem ipsum text</div>

</body>
</html>
```

The line `<title>{{ title }}</title>` allows the use of DTL (Django Template Language), enabling the injection of variables from the view into `index.html`.

To inject more context, modify `views.py` as follows:

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def djangorocks(request):
   return HttpResponse('This is a Jazzy Response')


def picture_detail(request, category, year=0, month=0, day=0):
   template = loader.get_template('apptwo/index.html')

   picture = {
      'filename' : 'Mottorad.jpg',
      'categories': ['color', 'landscape']
   }

   context = {
      'title': 'This is the picture detail',
      'category': category,
      'year': year,
      'month': month,
      'day': day,
      'picture': picture
   }
   return HttpResponse(template.render(context, request))
```

And modify `index.html` as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Index AppTwo</title>
</head>
<body>

{# Title block #}
<h1>{{ title }}</h1>

<div>
   category: {{category}} <br/>
   Year: {{year}} <br/>
   Month: {{month}} <br/>
   Day: {{day}} <br/>
</div>

<h2>Access variable detail</h2>
<div>
   filename: {{picture.filename}} <br/>
   first category: {{ picture.categories.0 }} <br/>
</div>

</body>
</html>
```

In the line `{{ picture.categories.0 }}`, the 0 allows accessing the first element in the list `'categories': ['color', 'landscape']` in `views.py`.

To see the changes, go to:
[http://127.0.0.1:8000/apptwo/pictures/portrait/2023/11/16/](http://127.0.0.1:8000/apptwo/pictures/portrait/2023/11/16/)


# Tags and filters in templates

## Tags:

Tags allow controlling the logic of the template.
- `{% comment "bla" %} ... {% endcomment %}`
- `{% if condition %} ... {% endif %}`
- `{% for ... %} ... {% endfor %}`
- The `<ul>` tag is used to create an unordered list, e.g.:
   - Banana
   - Orange
   - Apple
- The `<ol>` tag is used to create an ordered list, e.g.:
   1. Chapter 1
   2. Chapter 2
   3. Chapter 3
- The `<li>` tag is used to represent an item in a list. It must be contained in a parent element, such as an ordered list ( <ol> ), an unordered list ( <ul> ), or a menu ( <menu> ). In menus and unordered lists, list items are usually displayed with bullet points.
- The `<table>` tag defines an HTML table. It is the container for all the other table elements.
- The `<tr>` tag defines a table row. It is a child element of the `<table>` tag. Each `<tr>` element creates a new row in the table
- The `<td>` tag defines a table data cell. It is a child element of the `<tr>` tag, and can contain any content, such as text, images, links, etc. Each `<td>` element creates a new cell in the current row of the table.
- The `<th>` tag defines a table header cell. It is similar to the `<td>` tag, but it is used to indicate that the cell contains a header or label for a column or a row.

## Filters

Filters modify a variable before its display.
- `{{name|length %}` -> length of the variable `name`
- `{{name|default %}` -> empty only if `name` is empty
- `{{name|lower|truncatewords : 5 %}` -> display the content of `name` in lowercase and only the first 5 characters.
- The `join` filter joins items in an iterable into one string using a specified separator, e.g., `{{ picture.categories|join:', ' }}`. For example, if you have a list of categories, such as `['art', 'nature', 'animals']`, and you want to display them as a comma-separated string, you can use the join filter like this: `{{ picture.categories|join:', ' }}`. This will output `art, nature, animals`.

## Practice

Modify `index.html` as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Index AppTwo</title>
</head>
<body>

{# Title block #}
<h1>{{ title|title }}</h1>

<div>
   category: {{category}} <br/>
   Year: {{year}} <br/>
   Month: {{month}} <br/>
   Day: {{day}} <br/>
</div>

<h2>Access variable detail</h2>
<div>
   filename: {{picture.filename}} <br/>
   all categories:
   <ul>
      {% for category in picture.categories %}
      <li>{{ category }}</li>
      {% endfor %}
   </ul>

   all categories with filter:  {{ picture.categories|join:', ' }}
</div>

<h3>Picture table detail</h3>
{# Table block #}

<table>
   <tr style="background-color: {% cycle '#808080' '#d3d3d3' as rowcolors %}">
      <td>Resolution</td>
      <td>1920x1080</td>
   </tr>
   <tr style="background-color: {% cycle rowcolors %}">
      <td>Location</td>
      <td>Bizerte</td>
   </tr>
   <tr style="background-color: {% cycle rowcolors %}">
      <td>Filter</td>
      <td>No</td>
   </tr>
</table>

{% if day == 13 and month == 07 %}
<h3>Happy Birth Day !</h3>

{% elif day == 19 %}
<h3>Money is there !</h3>

{% else %}
<h4>Nothing fancy</h4>
{% endif %}

</body>
</html>
```

- The `<tr>` tag creates a row, and the `style` attribute changes its appearance.
- The `{% cycle '#808080' '#d3d3d3' as rowcolors %}` tag alternates between dark and light grey colors, naming the cycle `rowcolors`.
- The `{% cycle rowcolors %}` tag repeats the same cycle without specifying the arguments again.
- The rows have different colors in a striped pattern.

To see the changes, go to:
[http://127.0.0.1:8000/apptwo/pictures/portrait/2023/07/13/](http://127.0.0.1:8000/apptwo/pictures/portrait/2023/07/13/)


# Template et heritage:
