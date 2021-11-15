from django.db import models
from django.urls import reverse
from countries.models import Country


class City(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название города", unique=True)
    wealth = models.TextField(verbose_name="Богатство")
    area = models.FloatField(verbose_name="Площадь")
    population = models.FloatField(verbose_name="Население")
    pleasure = models.TextField(verbose_name="Удовлетворение")
    country = models.ForeignKey(Country, verbose_name="Страна", null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('city_info', kwargs={'city_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Город"
        verbose_name_plural = "Города"
