from django.contrib import admin
from regions.models import Region


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


admin.site.register(Region, RegionAdmin)


# Register your models here.
