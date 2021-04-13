from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, pagename):
    return HttpResponse(f'<h1>Welcome to the {pagename} </h1>')


def page2(request, email):
    return render(request, "sample.html", context={'email': email, 'location': 'Bangalore'})
