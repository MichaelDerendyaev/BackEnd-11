from regions.views import region_list, region_info
from django.urls import path

urlpatterns = [
    path('', region_list, name='region_list'),
    path('<int:region_id>/', region_info, name='region_info'),
]
