from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from .forms import SimpleClientForm
from .models import Client


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'clients/clients.html'
    model = Client
    context_object_name = 'clients'


client_list_view = ClientListView.as_view()


@login_required
def add_client(request):
    client_name = request.POST.get('client-name')
    form = SimpleClientForm(data={'input_text': client_name})
    if form.is_valid():
        form.save()

    context = {'clients': Client.objects.all()}
    return render(request, 'partials/client-list.html', context)


@login_required
@require_http_methods(['DELETE'])
def delete_client(request, pk):
    Client.objects.filter(pk=pk).delete()

    context = {'clients': Client.objects.all()}
    return render(request, 'partials/client-list.html', context)
