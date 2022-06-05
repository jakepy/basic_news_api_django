from ast import keyword
from django.shortcuts import render
from stocknews.settings import POLY_KEY
import requests


def home(request):
    url = f'https://api.polygon.io/v2/reference/news?&apiKey={POLY_KEY}'
    response = requests.get(url)
    data = response.json()
    results = data['results']

    context = {
        'results': results,
    }
    
    return render(request, 'polygonapp/home.html', context)