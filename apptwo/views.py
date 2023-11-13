from django.shortcuts import render
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a Jazzy Response')


def picture_detail(request,category):
    body = "Category={}".format(category)
    return HttpResponse(body)