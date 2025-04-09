from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"name": "test"}
    return render(request, "hello/index.html", context=context)


def brian(request):
    return HttpResponse("Hello, Brian!")


def david(request):
    return HttpResponse("Hello, David!")


def greet(request, name):
    context = {"name": name.capitalize()}
    return render(request, "hello/greet.html", context=context)
