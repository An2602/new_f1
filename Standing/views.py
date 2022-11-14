from django.http import HttpResponse
from django.template import loader
 
def Standing(request):
   template = loader.get_template('driver_standing.html')
   return HttpResponse(template.render())