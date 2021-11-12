from django.db import models


class Regions(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название региона", null=False, unique=True)
    capital = models.FloatField(verbose_name="Капитал", null=False)
    area = models.FloatField(verbose_name="Площадь", null=False)
    population = models.FloatField(verbose_name="Население", null=False)
    fertility = models.TextField(verbose_name="Плодородие", null=False)
    minerals = models.TextField(verbose_name="Полезные ископаемые", null=False)
