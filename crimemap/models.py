from django.db import models
from geoposition.fields import GeopositionField

class Crime(models.Model):
    case_number = models.IntegerField('Case Number')
    crime_date = models.DateTimeField('Date of Crime')
    comp_name = models.CharField('Complainant Name',max_length=200)
    #type_of_crime = models.CharField('Type of Crime',max_length=200)
    type_of_crime_choice = (
            ('as','Assault'),
            ('br','Burglary'),
            ('dp','Disturbing the Peace'),
            ('dv','Drug Violation'),
            ('hm','Homicide'),
            ('rb','Robbery'),
            ('th','Theft'),
            ('vd','Vandalism'),
            ('vt','Vehicle Theft'),
            ('ms','Miscellaneous'),
            )
    type_of_crime = models.CharField('Type Of Crime',max_length=20,choices=type_of_crime_choice,default='t1')
    position = GeopositionField('Location of Crime',default='28.4551918808319,77.02973962457577')
    dec = models.TextField('Description',max_length=500)

