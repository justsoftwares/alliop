from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('api/v1/', include('alliop.urls.api')),
]
