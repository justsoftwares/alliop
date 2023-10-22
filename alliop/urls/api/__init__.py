from django.urls import path, include

urlpatterns = [
    path('', include('alliop.urls.api.apps')),
    path('auth/', include('alliop.urls.api.auth')),
    path('schema/', include('alliop.urls.api.schema')),
]
