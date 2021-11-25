from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Client(models.Model):
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    national_id = models.CharField(_('National id'), max_length=80, null=True, blank=True)
    metadata = models.JSONField(_('Metadata'), null=True, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        display_name = f'{self.last_name}, {self.first_name}'
        return display_name


