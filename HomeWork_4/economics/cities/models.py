from django.db import models
from countries.models import Countries


class Cities(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название города", null=False, unique=True)
    wealth = models.TextField(verbose_name="Богатство", null=False)
    area = models.FloatField(verbose_name="Площадь", null=False)
    population = models.FloatField(verbose_name="Население", null=False)
    pleasure = models.TextField(verbose_name="Удовлетворение", null=False)
    country = models.ForeignKey(Countries, verbose_name="Страна", null=True, on_delete=models.SET_NULL)
