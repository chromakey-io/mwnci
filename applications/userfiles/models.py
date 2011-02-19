from django.db import models
from django.conf import settings

USERMEDIA_ROOT = getattr(settings, 'USERMEDIA_ROOT', 'user/')

class Type(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class File(models.Model):
    name = models.CharField(max_length=64)
    file = models.FileField(upload_to=USERMEDIA_ROOT)
    creation_date = models.DateField(auto_now_add=True)

    type = models.ForeignKey(Type)

    def get_absolute_url(self):
        return self.file.url

    def __unicode__(self):
        return self.name