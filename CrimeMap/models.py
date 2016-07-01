from django.db import models

class Crime(models.Model):
    img = models.ImageField('img', upload_to='CrimeMap/static/img')

    def cache(self):
        """Store image locally if we have a URL"""
        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0], 'rb'))
                    )
            self.save()
