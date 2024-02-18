from django.db import models


class Shed(models.Model):
    name = models.CharField('Название', max_length=15)
    kolvo = models.CharField('Количество', max_length=25)
    price = models.CharField('Стоимость', max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/katalog'


    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
