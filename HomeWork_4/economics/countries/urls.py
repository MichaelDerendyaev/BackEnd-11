from django.urls import path
from countries.views import country_list, country_info, country_create, country_delete, country_edit

urlpatterns = [
    path('list/', country_list, name='country_list'),
    path('create/', country_create, name='country_create'),
    path('delete/<int:country_id>/', country_delete, name='country_delete'),
    path('edit/<int:country_id>/', country_edit, name='country_edit'),
    path('describe/<int:country_id>/', country_info, name='country_info'),
]