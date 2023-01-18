from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.utils.html import format_html


def index(request):
    link = '/rango/about/'
    return HttpResponse("Rango says hey there partner!" + format_html('<a href="{}">About</a>', link))


def about(request):
    link = '/rango/'
    return HttpResponse("Rango says here is the about page." + format_html('<a href="{}">Index</a>', link))
