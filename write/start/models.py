from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Start(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
