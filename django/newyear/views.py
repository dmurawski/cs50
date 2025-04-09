from datetime import datetime

from django.shortcuts import render

# Create your views here.


def index(request):
    now = datetime.now()
    context = {
        "newyear": now.month == 1 and now.day == 1,
    }
    return render(request, "newyear/index.html", context=context)
