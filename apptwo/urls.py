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
    path("pictures/<str:category>/<int:year>/<int:month>/<dd:day>/", v2.picture_detail)
]
