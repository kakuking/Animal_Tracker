from django.shortcuts import render
from Dashboard.models import sighting, animal

import json
from django.http import HttpResponse, JsonResponse
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

def addSightingPage(request):
    all_sightings = sighting.objects.all()
    animals = animal.objects.all()
    ctx = {
        'sightings': all_sightings,
        'animals': animals
    }
        
    return render(request, 'Dashboard/addSighting.html', context=ctx)

@csrf_exempt
def filterTable(request):
    data = json.loads(request.body.decode('utf-8'))
    animal_list = data.get('animals', [])

    # print(animal_list)
    
    sightings = sighting.objects.exclude(animalType__in=animal_list)
    
    ctx = {
        'sightings': sightings
    }
        
    return render(request, 'Dashboard/table.html', context=ctx)
    
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

    return JsonResponse(data={
        'serialNum': sig.id,
        'dateTime': sig.dateTime
    })

