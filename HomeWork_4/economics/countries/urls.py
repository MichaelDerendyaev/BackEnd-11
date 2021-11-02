from django.urls import path
from countries.views import country_list, country_info

urlpatterns = [
    path('', country_list, name='country_list'),
    path('<int:country_id>/', country_info, name='country_info'),
]