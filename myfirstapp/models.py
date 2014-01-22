from django.db import models

# onetoone
class Truck(models.Model):
    trailer = models.OneToOneField('SmallTrailer')
    destinations = models.ManyToManyField('Destination')

class SmallTrailer(models.Model):
    capacity = models.IntegerField(default=5)

class Package(models.Model):
    transport = models.ForeignKey(SmallTrailer)

class Destination(models.Model):
    address = models.CharField(max_length=64)
    