from django.contrib import admin
from countries.models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


admin.site.register(Country, CountryAdmin)
