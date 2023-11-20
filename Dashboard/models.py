from django.db import models
from django.utils import timezone



class animal(models.Model):
    animal = models.CharField(default="Animal", max_length=255)

    def __str__(self):
        return self.animal

class sighting(models.Model):
    latitude = models.FloatField(default=17.543610)
    longitude = models.FloatField(default=78.574729)
    animalType = models.ForeignKey(animal, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.latitude}, {self.longitude}, {self.animalType}"

