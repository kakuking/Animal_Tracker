from django.shortcuts import render
from Dashboard.models import sighting, animal

# Create your views here.
def index(request):
    all_sightings = sighting.objects.all()

    return render(request, 'Dashboard/index.html', context={'sightings': all_sightings})
