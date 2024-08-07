from django.contrib import admin
from django.urls import path, include

from shop import urls as proudct_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(proudct_urls.urlpatterns))
]
