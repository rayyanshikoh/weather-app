import os
from django.http import Http404
from django.shortcuts import render, HttpResponse

import requests

import json

from dotenv import load_dotenv
load_dotenv()

api = str(os.getenv('APIKEY'))
# Create your views here.

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('search')
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        output = requests.get(link)
        output_json = output.json()
        if str(output_json['cod']) == '200':
            city = output_json['name']
            description = output_json['weather'][0]
            heading = description['main']
            detail = description['description']
            main = output_json['main']
            temp = f"{main['temp']}℉, feels like {main['feels_like']}℉"
            temp_max = main['temp_max']
            temp_min = main['temp_min']
            humidity = main['humidity']
            context = {
                'temp': temp,
                'city': city,
                'heading': heading,
                'detail': detail,
                'max_temp': temp_max,
                'min_temp': temp_min,
                'humidity': humidity
                }
        else:
            raise Http404()
        return render(request, 'weather/index.html', context)
    else:
        return render(request, 'weather/index.html')
    