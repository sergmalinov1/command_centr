from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return 'Имя пользователя - {0}'.format(self.customer_name)



