from chat.views import MessageViewSet, GroupViewSet, ChannelViewSet, InviteLinkViewSet
from common.routers import DefaultRouter

router = DefaultRouter()
router.register('message', MessageViewSet)
router.register('group', GroupViewSet)
router.register('channel', ChannelViewSet)
router.register('invite-link', InviteLinkViewSet)
urlpatterns = router.urls
