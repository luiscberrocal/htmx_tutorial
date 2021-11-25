from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Client


class ClientListView(ListView):
    template_name = 'clients/clients.html'
    model = Client
    context_object_name = 'clients'


client_list_view = ClientListView.as_view()
