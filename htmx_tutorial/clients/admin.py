from django.contrib import admin

# Register your models here.
from htmx_tutorial.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'display_order', 'created')
    search_fields = ('last_name',)
