from rest_framework.response import Response
from rest_framework.views import APIView
from _api_info.utils.apiinfo import ipinfo


class MyIpInfo(APIView):
    def get(self, request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        context = ipinfo(ip)
        return Response(context)

    def post(self, request):
        ip = request.data.get('ip')
        context = ipinfo(ip)
        return Response(context)
