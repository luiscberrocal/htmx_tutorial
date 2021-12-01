from django import forms
from django.core.exceptions import ValidationError

from htmx_tutorial.clients.models import Client
from htmx_tutorial.clients.utils import get_max_order


class SimpleClientForm(forms.Form):
    input_text = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(SimpleClientForm, self).clean()
        input_text = cleaned_data['input_text'].title()
        if ',' in input_text:
            parts = input_text.split(',')
            if len(parts) == 2:
                cleaned_data['last_name'] = parts[0]
                cleaned_data['first_name'] = parts[1]
            else:
                msg = 'More than one comma'
                raise ValidationError(msg)
        else:
            parts = input_text.split(' ')
            if len(parts) < 2:
                msg = 'Need to include first and last name'
                raise ValidationError(msg)
            else:
                cleaned_data['last_name'] = parts[-1]
                cleaned_data['first_name'] = ' '.join(parts[:-1])
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        if Client.objects.filter(first_name=data['first_name'], last_name=data['last_name']).exists():
            client = Client.objects.get(first_name=data['first_name'], last_name=data['last_name'])
            client.display_order = get_max_order()
            client.is_active = True
            client.save()
        else:
            client = Client.objects.create(first_name=data['first_name'], last_name=data['last_name'],
                                           display_order=get_max_order())
        # client, _ = Client.objects.get_or_create(first_name=data['first_name'], last_name=data['last_name'])
        # if not client.is_active:
        #     client.is_active = True
        #     client.save()
        return client

