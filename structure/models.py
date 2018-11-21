from django.db import models

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
        return 'Название - {0}, Статус {1} '.format(self.name, self.status_of_world)


class Customer_Account(models.Model):
    name = models.CharField(max_length=50)
    world = models.ForeignKey(World_version, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название - {0}, Статус {1} '.format(self.name, self.world.name)