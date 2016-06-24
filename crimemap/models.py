from django.db import models
from geoposition.fields import GeopositionField

class Crime(models.Model):
    def __str__(self):
        return 'Case Number: {}'.format(self.case_number)
    case_number = models.IntegerField('Case Number',primary_key = True)
    crime_date = models.DateTimeField('Date of Crime')
    comp_name = models.CharField('Complainant Name',max_length=200)
    #type_of_crime = models.CharField('Type of Crime',max_length=200)
    type_of_crime_choice = (
            ('Assault','Assault'),
            ('Burglary','Burglary'),
            ('Disturbing the Peace','Disturbing the Peace'),
            ('Drug Violation','Drug Violation'),
            ('Homicide','Homicide'),
            ('Robbery','Robbery'),
            ('Theft','Theft'),
            ('Vandalism','Vandalism'),
            ('Vehicle Theft','Vehicle Theft'),
            ('Miscellaneous','Miscellaneous'),
            )
    type_of_crime = models.CharField('Type Of Crime',max_length=20,choices=type_of_crime_choice,default='Assault')
    position = GeopositionField('Location of Crime',default='28.4551918808319,77.02973962457577')
    dec = models.TextField('Description',max_length=500)

