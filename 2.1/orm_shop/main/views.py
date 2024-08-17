from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from main.models import Car, Client, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def search_view(request):
    cars = Car.objects.filter(model=request.GET.get('q'))
    context = {
        'cars': cars
    }
    template_name = 'main/list.html'
    return render(request, template_name, context)


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponse('Автомобиль не найден')
    else:
        context = {
            'car': car
        }
    template_name = 'main/details.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car__id=car_id)
        context = {
            'car': car,
            'sales': sales
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
