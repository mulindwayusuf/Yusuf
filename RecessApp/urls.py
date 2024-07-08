from django.urls import path
from . import views

urlpatterns = [
    path('', views.moisture_list, name='moisture_list'),
]
