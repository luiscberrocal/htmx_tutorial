from django.db.models import Max

from htmx_tutorial.clients.models import Client


def get_max_order() -> int:
    clients_displayed = Client.objects.filter(is_active=True)
    if not clients_displayed.exists():
        return 1
    else:
        current_max = clients_displayed.aggregate(max_order=Max('display_order'))['max_order']
        return current_max + 1


def reorder():
    clients_displayed = Client.objects.filter(is_active=True)
    if not clients_displayed.exists():
        return
    number_of_clients_displayed = clients_displayed.count()
    new_ordering = range(1, number_of_clients_displayed + 1)

    for order, client in zip(new_ordering, clients_displayed):
        client.display_order = order
        client.save()
