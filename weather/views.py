import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def get_weather_data(city_name):
    api_key = '4a51993e0b7a026d891dc93d85e3a0a5'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def index(request):
    form = CityForm()
    weather_data = {}

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            weather_data = get_weather_data(city_name)
            City.objects.create(name=city_name)

    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data})
