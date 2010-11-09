from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=512)
    logo = models.ImageField(upload_to='social-logos/')
    order = models.IntegerField(default = 0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
		return self.name