from django.forms import ModelForm
from .models import Race, Standing_in_race

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['race_name', 'race_type', 'race_date', 'fastest_driver']

class StandingForm(ModelForm):
    class Meta:
        model = Standing_in_race
        fields = ['driver', 'race', 'standing']