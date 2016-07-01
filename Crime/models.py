from django.db import models
from geoposition.fields import GeopositionField

class Crime(models.Model):
    def __str__(self):
        return 'Case Register Number: {}'.format(self.case_no)
    case_no = models.CharField('Case Register Number',max_length=50)
    crime_date = models.DateTimeField('Date of Crime')
    comp_name = models.CharField('Complaiant Name',max_length=50)
    type_crime = models.ForeignKey('Type_Of_Crime.Type_Of_Crime',related_name='type_of_crime')
    thana = models.ForeignKey('Thana.Thana',related_name='thana')
    sadar = models.ForeignKey('Sadar.Sadar',related_name='sadar')
    position = GeopositionField('Location of Crime',default='28.455191808319,77.02973962457577')
    dec = models.TextField('Description',max_length=500)
# Create your models here.
