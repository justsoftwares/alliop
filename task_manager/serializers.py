from common.serializers import get_serializer
from task_manager.models import Period, Task, Team, Table, Project

PeriodSerializer = get_serializer(Period)
TaskSerializer = get_serializer(Task)
TeamSerializer = get_serializer(Team)
TableSerializer = get_serializer(Table)
ProjectSerializer = get_serializer(Project)
