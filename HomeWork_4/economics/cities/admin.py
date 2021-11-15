from django.contrib import admin
from cities.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


admin.site.register(City, CityAdmin)
