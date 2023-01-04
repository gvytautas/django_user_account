from django.shortcuts import render, redirect
from .models import Service, Order
from .forms import VehicleModelForm, VehicleForm
from django.contrib import messages


# CRUD > Create Read Update Delete


# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_services(request):
    services = Service.objects.values()
    return render(request, 'show_services.html', context={'services': services})


def show_orders(request):
    orders = Order.objects.filter(vehicle__model__brand__startswith='Brand').all()
    return render(request, 'show_orders.html', context={'orders': orders})


def add_vehicle_model(request):
    if request.method == 'POST':
        form = VehicleModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_vehicle_model.html', context={'form': form})
    else:
        form = VehicleModelForm()
    return render(request, 'add_vehicle_model.html', context={'form': form})


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.client = request.user
            vehicle.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_vehicle.html', context={'form': form})
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', context={'form': form})
