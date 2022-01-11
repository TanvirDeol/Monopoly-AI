from django.db import models

# Create your models here.
class Interactor(models.Model):
    pos = models.IntegerField(default=-1)
    money = models.IntegerField(default=0)
    propertyBought = models.IntegerField(default=-1)
    propertyExpanded = models.IntegerField(default=-1)
    housesBought = models.IntegerField(default=0)
