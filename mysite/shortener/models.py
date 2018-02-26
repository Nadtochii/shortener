from django.db import models

# Create your models here.

class Shortener(models.Model):
    long_link  = models.CharField(max_length=60)
    short_link = models.CharField(max_length=32)
    
    def __str__(self):
        return u'%s %s' % (self.long_link, self.short_link)
