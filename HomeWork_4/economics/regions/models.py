from django.db import models
from django.urls import reverse


class Region(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название региона", unique=True)
    capital = models.FloatField(verbose_name="Капитал")
    area = models.FloatField(verbose_name="Площадь")
    population = models.FloatField(verbose_name="Население")
    fertility = models.TextField(verbose_name="Плодородие")
    minerals = models.TextField(verbose_name="Полезные ископаемые")

    def get_absolute_url(self):
        return reverse('region_info', kwargs={'region_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
