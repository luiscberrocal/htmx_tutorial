from django.urls import path

from .views import client_list_view

app_name = 'clients'

urlpatterns = [
    path('clients/', client_list_view, 'clients-list')
]
