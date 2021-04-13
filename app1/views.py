from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to the first page</h1>")


def page2(request):
    return render(request, "sample.html")
