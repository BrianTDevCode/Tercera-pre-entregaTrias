

from django.urls import path
from . import views

app_name = "consesionario"

urlpatterns = [
    path("", views.home, name='index'),
    path("customer/", views.customers_view, name='customers'),
    path("garage/", views.garages_view, name='garages'),
    path("car/", views.cars_view, name='cars'),
    path("list/", views.list_view, name='list'),

]
