from django.db import models
from django.urls import reverse
from regions.models import Region


class Country(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название страны", unique=True)
    wealth = models.TextField(verbose_name="Богатство")
    area = models.FloatField(verbose_name="Площадь")
    population = models.FloatField(verbose_name="Население")
    pleasure = models.TextField(verbose_name="Удовлетворение")
    region = models.ForeignKey(Region, verbose_name="Регион", null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('country_info', kwargs={'country_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
