from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from crimemap.models import Crime

def index(request):
    position = Crime.objects.order_by('-case_number')
    context = {
        'position': position,
    }
    template = loader.get_template('map/index.html')
    return HttpResponse(template.render(context, request))
