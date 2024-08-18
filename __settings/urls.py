
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/ipinfo/', include('_api_info.api_urls')),
    path('api/v1/domain/', include('_domain_info.api_urls'))
]
