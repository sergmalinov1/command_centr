from django.db import models

class Landscape(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=50)

    def __str__(self):
        return 'Название - {0}, Картинка {1} '.format(self.name, self.img)


class Cell(models.Model):
    name = models.CharField(max_length=50)
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    landscape = models.ForeignKey(Landscape, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название:{0} Хоординаты Х\Y - {1} \ {2} '.format(self.name, self.coord_x, self.coord_y)