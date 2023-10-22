from common.viewsets import get_viewset
from task_manager.serializers import (PeriodSerializer, TaskSerializer, TeamSerializer,
                                      TableSerializer, ProjectSerializer)

PeriodViewSet = get_viewset(PeriodSerializer)
TaskViewSet = get_viewset(TaskSerializer, _show_user_fields=['for_user'])
TeamViewSet = get_viewset(TeamSerializer, _show_user_fields=['members'])
TableViewSet = get_viewset(TableSerializer)
ProjectViewSet = get_viewset(ProjectSerializer, _show_user_fields=['team__members'])
