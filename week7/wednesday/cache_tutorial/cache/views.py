from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# @cache_page(900)
import requests


def index(request):
    data = {"request": request}
    return render(request, "index.html", data)


def weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco,USA"

    weather_data = cache.get(url)
    if not weather_data:
        response = requests.get(url)
        weather_data = response.json()
        cache.set(url, weather_data, 300)

    data = {"weather_data": weather_data}

    return render(request, "weather.html", data)


def weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco,USA"

    weather_data = cache.get(url)
    if not weather_data:
        response = requests.get(url)
        weather_data = response.json()
        cache.set(url, weather_data, 300)

    data = {"weather_data": weather_data}

    return render(request, "weather.html", data)