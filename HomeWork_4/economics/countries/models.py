from django.db import models
from regions.models import Regions


class Countries(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название страны", null=False, unique=True)
    wealth = models.TextField(verbose_name="Богатство", null=False)
    area = models.FloatField(verbose_name="Площадь", null=False)
    population = models.FloatField(verbose_name="Население", null=False)
    pleasure = models.TextField(verbose_name="Удовлетворение", null=False)
    region = models.ForeignKey(Regions, verbose_name="Регион", null=True, on_delete=models.SET_NULL)
