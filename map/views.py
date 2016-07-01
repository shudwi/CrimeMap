from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from Crime.models import Crime
from Thana.models import Thana
from Sadar.models import Sadar

def index(request):
    position_crime = Crime.objects.all()
    position_thana = Thana.objects.all()
    position_sadar = Sadar.objects.all()
    context = {
        'position_crime': position_crime,
        'position_thana': position_thana,
        'position_sadar': position_sadar,
    }
    template = loader.get_template('map/index.html')
    return HttpResponse(template.render(context, request))
