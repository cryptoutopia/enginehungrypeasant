from django.shortcuts import render
from urllib.request import Request
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from api.models import *
import json

# Create your views here.


def getAll(requset):

    response = {
        "restaurants": [],
        "menus": {},
        "contacts": {}
    }

    try:

        restaurants = list(Restaurant.objects.all())
        dailyMenus = list(DailyMenu.objects.all())
        contacts = Contact.objects.all().filter(type='P')

        for e in restaurants:
            response["restaurants"].append({
                "name": e.name,
                "key": e.key,
            })

            response["menus"][e.key] = []

        for e in dailyMenus:
            response["menus"][e.restaurant.key].append({
                'day': e.day,
                'meal': e.meal
            })

        for e in contacts:
            response["contacts"][e.restaurant.key] = e.value
    
    except Exception as e:
        print(e)

    return HttpResponse(json.dumps(response), content_type=("application/json"));


@csrf_exempt
def update(request):
    
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request')

    try:
        data = json.loads(request.body)
        restaurant = Restaurant.objects.get(key=data['restaurant'])

        DailyMenu.objects.filter(restaurant=restaurant).delete()

        # recreate menus    
        for e in DailyMenu.DAYS:

            if e[0] in data:

                entry = DailyMenu(restaurant=restaurant, day=e[0], meal=data[e[0]])
                entry.save()
        
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(e)

