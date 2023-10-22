from common.routers import DefaultRouter
from task_manager.views import PeriodViewSet, TaskViewSet, TeamViewSet, TableViewSet, ProjectViewSet

router = DefaultRouter()
router.register('period', PeriodViewSet)
router.register('task', TaskViewSet)
router.register('team', TeamViewSet)
router.register('table', TableViewSet)
router.register('project', ProjectViewSet)
urlpatterns = router.urls
