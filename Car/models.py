from django.db import models


class Car(models.Model):
   name = models.CharField(max_length=100, null=False)
   created_time = models.DateTimeField(auto_now_add=True)
   updated_time = models.DateTimeField(auto_now=True)


   def __str__(self):
        return self.name + str(self.drivers.all())
        #   + ", score: " + self.score + str(self.drivers.all())

   def team_scores(self):
        team_score = 0
        drivers = self.drivers.all()
        for driver in drivers:
            team_score += driver.score
        return team_score