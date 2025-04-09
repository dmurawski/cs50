from django.shortcuts import render

# Create your views here.

tasks = ["foo", "bar", "baz"]


def index(request):
    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context=context)


def add(request):
    return render(request, "tasks/add.html")
