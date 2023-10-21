from django.shortcuts import render
from Dashboard.models import sighting, animal

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    all_sightings = sighting.objects.all()
    animals = animal.objects.all()
    ctx = {
        'sightings': all_sightings,
        'animals': animals
    }
    return render(request, 'Dashboard/index.html', context=ctx)

@csrf_exempt
def addSighting(request):
    if request.method != "POST":
        return
    
    data = json.loads(str(request.body, encoding='utf-8'))

    # print(request.body)

    animalType = data.get("animal")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    animalOfType = animal.objects.get(pk=animalType)

    sig = sighting(animalType=animalOfType,latitude=latitude,longitude=longitude)
    sig.save()

    print("Added Sighting");

    return HttpResponse(status=200)

