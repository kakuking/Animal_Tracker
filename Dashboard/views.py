from django.shortcuts import render
from Dashboard.models import sighting, animal

import json
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    all_sightings = sighting.objects.all()
    animals = animal.objects.all()
    
    curTime = timezone.now()

    all_sightings = [sight for sight in all_sightings if curTime - sight.dateTime <= timezone.timedelta(hours=5)]
    
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

    curTime = timezone.now()

    sightings = [sight for sight in sightings if curTime - sight.dateTime <= timezone.timedelta(hours=1)]
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
    id_submitted = data.get("id_submitted")

    animalOfType = animal.objects.get(pk=animalType)

    if(len(id_submitted) < 13):
        return HttpResponse(status=400)

    sig = sighting(animalType=animalOfType,latitude=latitude,longitude=longitude,id_submitted=id_submitted)
    sig.save()

    print("Added Sighting");

    return JsonResponse(data={
        'serialNum': sig.id,
        'dateTime': sig.dateTime
    })

def guidelinesPage(request):
    return render(request, 'Dashboard/guidelines.html')

def discussionsPage(request):
    return render(request, 'Dashboard/discussions.html')