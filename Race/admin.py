from django.contrib import admin
 
from Race.models import Race, Standing_in_race
 
# # Register your models here.
admin.site.register(Race)
admin.site.register(Standing_in_race)