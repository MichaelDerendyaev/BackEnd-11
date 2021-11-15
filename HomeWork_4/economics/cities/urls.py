from cities.views import city_list, city_info, city_create, city_edit, city_delete
from django.urls import path

urlpatterns = [
    path('list/', city_list, name='city_list'),
    path('create/', city_create, name='city_create'),
    path('edit/<int:city_id>/', city_edit, name='city_edit'),
    path('delete/<int:city_id>/', city_delete, name='city_delete'),
    path('detail/<int:city_id>/', city_info, name='city_info'),
]
