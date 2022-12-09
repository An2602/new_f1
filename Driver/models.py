from django.db import models

from Car.models import Car

# Create your models here.

# Id (PK)
# Name
# Country
# Car
# Score
# Standing
 
class Driver(models.Model):
   name = models.CharField(max_length=100, null=False)
   country = models.CharField(max_length=100, null=False)
   car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="drivers")
   score = models.SmallIntegerField(null=False)
   created_time=models.DateTimeField(auto_now_add=True)
   updated_time=models.DateTimeField(auto_now=True)
   image = models.ImageField(null=True, blank=True, default='/placeholder.png')

   def __str__(self):
        return self.name 


      #   + ", score: " + self.score