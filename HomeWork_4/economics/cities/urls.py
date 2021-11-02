from cities.views import city_list, city_info
from django.urls import path

urlpatterns = [
    path('', city_list, name='city_list'),
    path('<int:city_id>/', city_info, name='city_info'),
]
