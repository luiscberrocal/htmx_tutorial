from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
from django.db import models


class AuditableModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_%(class)s", null=True, on_delete=models.SET_NULL
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="modified_%(class)s", null=True, on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True


class Client(AuditableModel, TimeStampedModel):
    name = models.CharField(_('Name'), max_length=120)
    national_id = models.CharField(_('National id'), max_length=80, unique=True)
    verification_digit = models.CharField(_('Verification  digit'), max_length=3, null=True, blank=True)
    metadata = models.JSONField(_('Metadata'), null=True, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    display_order = models.PositiveIntegerField(_('Display Order'), default=0)

    class Meta:
        ordering = ('display_order', 'name')

    def __str__(self):
        return self.name
