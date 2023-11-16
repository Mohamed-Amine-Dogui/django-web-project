from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def djangorocks(request):
    return HttpResponse('This is a Jazzy Response')


def picture_detail(request,category, year=0, month=0, day=0  ):
    template = loader.get_template('apptwo/index.html')
    return HttpResponse(template.render({}, request))