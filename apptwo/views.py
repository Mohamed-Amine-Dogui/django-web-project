from django.shortcuts import render
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a Jazzy Response')


def picture_detail(request,category, year=0, month=1 ):
    body = "Category={}, year = {}, month = {}".format(category, year, month )
    return HttpResponse(body)