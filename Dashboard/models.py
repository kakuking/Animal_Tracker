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
    id_submitted = models.CharField(default="2020ABCD0001H", max_length=13, null=False)
    
    def __str__(self):
        return f"{self.latitude}, {self.longitude}, {self.animalType}"

