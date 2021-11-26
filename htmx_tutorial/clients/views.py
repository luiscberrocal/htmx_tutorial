from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Client


class ClientListView(ListView):
    template_name = 'clients/clients.html'
    model = Client
    context_object_name = 'clients'


client_list_view = ClientListView.as_view()


def add_client(request):
    client_name = request.POST.get('client-name')
    name_parts = client_name.split(',')
    Client.objects.create(first_name=name_parts[1], last_name=name_parts[0])

    context = {'clients': Client.objects.all()}
    return render(request, 'partials/client-list.html', context)


def delete_client(request, pk):
    Client.objects.filter(pk=pk).delete()

    context = {'clients': Client.objects.all()}
    return render(request, 'partials/client-list.html', context)
