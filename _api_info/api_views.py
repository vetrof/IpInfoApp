from rest_framework.response import Response
from rest_framework.views import APIView
from _api_info.utils.apiinfo import ipinfo


class IpInfo(APIView):
    def get(self, request, ip=None):
        if ip:
            context = ipinfo(ip)
            return Response(context)
        else:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
            context = ipinfo(ip)
            return Response(context)
