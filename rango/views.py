from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.utils.html import format_html


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

    #link = '/rango/about/'
    #return HttpResponse("Rango says hey there partner! " + format_html('<a href="{}">About</a>', link))


def about(request):
    link = '/rango/'
    return HttpResponse("Rango says here is the about page. " + format_html('<a href="{}">Index</a>', link))
