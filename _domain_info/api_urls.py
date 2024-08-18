from django.urls import include, path

from _domain_info.api_views import DomainInfo

urlpatterns = [
    path('<str:ip_or_domain>', DomainInfo.as_view(), name='IpInfo')
]