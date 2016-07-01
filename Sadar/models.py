from django.db import models
from geoposition.fields import GeopositionField

class Sadar(models.Model):
    def __str__(self):
        return 'Sadar: {}'.format(self.name)
    name = models.CharField('Sadar Name',max_length=50)
    location = GeopositionField('Location of Sadar',default='28,77')
    marker = models.ImageField('Marker',upload_to='static/Sadar/img')

# Create your models here.
