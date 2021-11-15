from regions.views import region_list, region_info, region_create, region_delete, region_edit
from django.urls import path

urlpatterns = [
    path('list/', region_list, name='region_list'),
    path('create/', region_create, name='region_create'),
    path('delete/<int:region_id>/', region_delete, name='region_delete'),
    path('detail/<int:region_id>/', region_info, name='region_info'),
    path('edit/<int:region_id>/', region_edit, name='region_edit'),
]
