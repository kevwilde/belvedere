from django.contrib import admin
from apps.infrastructure.models import Server, Environment, Deployment, ApplicationEndpoint


admin.site.register(Server)
admin.site.register(Environment)
admin.site.register(Deployment)
admin.site.register(ApplicationEndpoint)
