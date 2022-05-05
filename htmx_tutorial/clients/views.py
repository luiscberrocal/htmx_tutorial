from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from .forms import SimpleClientForm
from .models import Client


@login_required
def add_client(request):
    client_name = request.POST.get('client-name')
    form = SimpleClientForm(data={'input_text': client_name})
    if form.is_valid():
        form.save()
    else:
        messages.error(request, _('Error parsing client name.'))

    context = {'clients': Client.objects.filter(is_active=True).all()}
    return render(request, 'partials/client-list.html', context)


@login_required
@require_http_methods(['DELETE'])
def delete_client(request, pk):
    Client.objects.filter(pk=pk).update(is_active=False, display_order=0)

    context = {'clients': Client.objects.filter(is_active=True).all()}
    return render(request, 'partials/client-list.html', context)


@login_required
@require_http_methods(['POST'])
def search_client(request):
    search_text = request.POST.get('search')
    results = Client.objects.filter(last_name__icontains=search_text, is_active=False)
    context = {'results': results}
    return render(request, 'partials/search-results.html', context)


@login_required
def clear(request):
    return HttpResponse('')


@login_required
@require_http_methods(['POST'])
def sort_clients(request):
    client_pks_order = request.POST.getlist('client_order')
    client_list = []
    for idx, client_pk in enumerate(client_pks_order, start=1):
        client = Client.objects.get(pk=client_pk)
        client.display_order = idx
        client.save()
        client_list.append(client)

    return render(request, 'partials/client-list.html', {'clients': client_list})


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list-client')


client_create_view = ClientCreateView.as_view()


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list-client')


client_update_view = ClientUpdateView.as_view()


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'client_list'
    paginate_by = 10


client_list_view = ClientListView.as_view()


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list-client')


client_delete_view = ClientDeleteView.as_view()


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


client_detail_view = ClientDetailView.as_view()
