from django import forms
from django.core.exceptions import ValidationError

from htmx_tutorial.clients.models import Client


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
        client, _ = Client.objects.get_or_create(first_name=data['first_name'], last_name=data['last_name'])
        if not client.is_active:
            client.is_active = True
            client.save()
        return client

