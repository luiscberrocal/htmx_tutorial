from django.urls import path

from .views import client_list_view, add_client, delete_client, search_client, clear, sort_clients, detail_client

app_name = 'clients'

urlpatterns = [
    path('clients/', client_list_view, name='clients-list'),
    path('add-client/', add_client, name='add-client'),
    path('delete-client/<int:pk>/', delete_client, name='delete-client'),
    path('detail-client/<int:pk>/', detail_client, name='detail-client'),
    path('search-client/', search_client, name='search-client'),
    path('sort-client/', sort_clients, name='sort-client'),
    path('clear/', clear, name='clear-messages'),
]
