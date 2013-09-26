from django.db import models


class Application(models.Model):
    """
    Abstract representation of an application that can be monitored.
    """
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
