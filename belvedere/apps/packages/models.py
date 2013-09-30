from django.db import models
from apps.applications.models import Application


class SystemPackage(models.Model):
    """
    A system package associated with the application.
    """
    name = models.CharField(max_length=64)

    application = models.ForeignKey(Application, null=True, blank=True)

    def __unicode__(self):
        return self.name
