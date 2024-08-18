from django.urls import include, path

from _api_info import api_views

urlpatterns = [
    path('', api_views.IpInfo.as_view(), name='IpInfo')
]