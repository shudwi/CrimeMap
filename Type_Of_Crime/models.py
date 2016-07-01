from django.db import models

# Create your models here.
class Type_Of_Crime(models.Model):
    def __str__(self):
        return 'Type Of Crime: {}'.format(self.name)
    class Meta:
        verbose_name="Type Of Crime"
        verbose_name_plural="Type Of Crime"
    name = models.CharField('Type of Crime', max_length=50)
    img = models.ImageField('Marker Image', upload_to='static/mark')
