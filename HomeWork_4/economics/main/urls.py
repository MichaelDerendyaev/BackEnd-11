from django.urls import path
from main.views import render_home

urlpatterns = [
    path('', render_home, name='render_home'),
]