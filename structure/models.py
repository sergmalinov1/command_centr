from django.db import models
#from customer.models import Customer
from django.contrib.auth.forms import User

# Create your models here.
class World_version(models.Model):
    STATUS_OF_WORLD = (
        ('enable', '_enable'),
        ('disable', '_disable'),
        ('comingsoon', '_comingsoon'),
    )

    name = models.CharField(max_length=50)
    status_of_world = models.CharField(max_length=10, choices=STATUS_OF_WORLD)

    def __str__(self):
        return 'Название - {0}'.format(self.name)

class Customer_Account(models.Model):
    name = models.CharField(max_length=50)
    world = models.ForeignKey(World_version, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название - {0}, Статус {1}'.format(self.name, self.world.name)

class Country(models.Model):
    name = models.CharField(max_length=50)
    world = models.ForeignKey(World_version, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название - {0}'.format(self.name)

class Clan(models.Model):
    name = models.CharField(max_length=50)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название - {0}'.format(self.name)