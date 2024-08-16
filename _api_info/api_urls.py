from django.urls import include, path

from _api_info import api_views

urlpatterns = [
    path('my/', api_views.MyIpInfo.as_view(), name='myIpInfo')
]