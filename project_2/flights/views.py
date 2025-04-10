from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.


def index(request):
    context = {
        "flights": Flight.objects.all(),
    }
    return render(request, "flights/index.html", context=context)


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight),
    }
    return render(request, "flights/flight.html", context=context)


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(
            reverse(
                "flight",
                args=(flight.id,),
            )
        )
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
    }
    return render(request, "flights/flight.html", context=context)
    return render(request, "flights/flight.html", context=context)
