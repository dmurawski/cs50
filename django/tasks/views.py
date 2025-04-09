from django import forms
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

# Create your views here.


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    context = {"tasks": request.session["tasks"]}
    return render(request, "tasks/index.html", context=context)


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(request, "tasks/add.html", {"form": NewTaskForm()})


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
