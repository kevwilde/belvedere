from django.db import models
from apps.applications.models import Application


class ApplicationEndpoint(models.Model):
    """
    Describes the URI location of the deployed web application.
    """
    deployment = models.ManyToManyField('Deployment')
    URI = models.CharField(max_length=200)

    def __unicode__(self):
        return self.URI


class Deployment(models.Model):
    """
    Describes the deployment of an application on a server in the
    infrastructure
    """
    application = models.ForeignKey(Application)
    server = models.ForeignKey('Server')

    def __unicode__(self):
        return "{0} [{1}]".format(self.application.name, self.server.hostname)


class Server(models.Model):
    """
    A Server in the infrastructure
    """
    hostname = models.CharField(max_length=100)
    environment = models.ForeignKey('Environment')

    def installed_applications(self):
        """
        Returns a list of installed applications on the server
        """
        deployments = self.deployment_set.all()
        return [d.application for d in deployments]

    def short_hostname(self):
        return self.hostname.split('.')[0]

    def __unicode__(self):
        return "{0} [{1}]".format(self.hostname, self.environment.name)


class Environment(models.Model):
    """
    A classificiation of purpose withing the infrastructure
    """
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
