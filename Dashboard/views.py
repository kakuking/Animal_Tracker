from django.shortcuts import render
from Dashboard.models import sighting, animal

# Create your views here.
def index(request):

    return render(request, 'Dashboard/index.html')
