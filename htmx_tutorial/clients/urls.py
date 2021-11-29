from django.urls import path

from .views import client_list_view, add_client, delete_client, search_client, clear

app_name = 'clients'

urlpatterns = [
    path('clients/', client_list_view, name='clients-list'),
    path('add-client/', add_client, name='add-client'),
    path('delete-client/<int:pk>/', delete_client, name='delete-client'),
    path('search-client/', search_client, name='search-client'),
    path('clear/', clear, name='clear-messages'),
]
