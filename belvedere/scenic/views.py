import json
from django.http.response import Http404, HttpResponse
from django.views.generic.base import View
from . import utils

class JSONView(View):

    def get_data(self):
        return dict()

    def get(self, request, *args, **kwargs):
        data = self.get_data()
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )


class PackageDetailView(JSONView):

    def get_data(self):
        self.package_name = self.kwargs.get('pkgname', None)
        if self.package_name:
            return utils.local_package_information(self.package_name)
        else:
            raise Http404
