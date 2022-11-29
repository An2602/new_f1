from django.db import models
from enum import Enum
from Driver.models import Driver

# Id (PK)
# race_name
# race_standing
# race_type



class Race(models.Model):

    class Race_type(models.IntegerChoices):
        regular = 1, "Regular race"
        sprint = 2, "Sprint race"
        
    race_name = models.CharField(max_length=100, null=False)
    fastest_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race_type = models.SmallIntegerField(null=False, default = Race_type.regular, choices=Race_type.choices)
    race_date = models.DateField(null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.race_name

class Standing_in_race(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    standing = models.SmallIntegerField(null=False)

    # def __str__(self):
    #     return self.driver.name, self.race.race_name, "standing: "  + str(self.standing)
