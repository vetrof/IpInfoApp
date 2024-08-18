from rest_framework.response import Response
from rest_framework.views import APIView
from _domain_info.service.ip_api_client import ip_api


class DomainInfo(APIView):

    def get(self, request, ip_or_domain):
        context = ip_api(ip_or_domain)
        return Response(context)
