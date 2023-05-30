from django.shortcuts import render
from .models import Cars


# Create your views here.
def index(request):
    return render(request, 'automarket/index.html')


def cars(request):
    cars = Cars.objects.all()
    return render(request, 'automarket/cars.html', {'cars': cars})


def about(request):
    return render(request, 'automarket/about.html')


def contact(request):
    return render(request, 'automarket/contact.html')
