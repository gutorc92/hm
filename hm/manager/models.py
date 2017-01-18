from django.db import models
from django.conf import settings

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)

class Home(models.Model):
    name = models.CharField(max_length=200)

class Living(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="member_of",
                               on_delete=models.DO_NOTHING)
    family = models.ForeignKey(Family, related_name="family",
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True)
    home =  models.ForeignKey(Home, related_name="home",
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)


