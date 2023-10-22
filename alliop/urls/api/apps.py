from django.urls import path, include

urlpatterns = [
    path('task-manager/', include('task_manager.urls')),
    path('chat/', include('chat.urls'))
]
