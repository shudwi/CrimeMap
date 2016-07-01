from django.db import models
from geoposition.fields import GeopositionField

class Thana(models.Model):
    def __str__(self):
        return 'Thana: {}'.format(self.name)
    name = models.CharField('Thana Name', max_length=50)
    location = GeopositionField('Location of Thana',default='28,77')
    marker = models.ImageField('Marker',upload_to='static/Thana/img')
# Create your models here.
