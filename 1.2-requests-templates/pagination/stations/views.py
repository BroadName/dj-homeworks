from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    LST = list(reader)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(LST, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
