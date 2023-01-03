from django.shortcuts import render
from .models import Service, Order


# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_services(request):
    services = Service.objects.values()
    return render(request, 'show_services.html', context={'services': services})


def show_orders(request):
    orders = Order.objects.filter(vehicle__model__brand__startswith='Brand').all()
    return render(request, 'show_orders.html', context={'orders': orders})
