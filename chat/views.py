from rest_framework.decorators import action
from rest_framework.response import Response

from chat.models import Message, Group, Channel, InviteLink
from chat.serializers import MessageSerializer, GroupSerializer, ChannelSerializer, InviteLinkSerializer
from common.viewsets import get_viewset

MessageViewSet = get_viewset(MessageSerializer, Message)
GroupViewSet = get_viewset(GroupSerializer, Group)


class ChannelViewSet(get_viewset(ChannelSerializer, Channel)):
    @action(detail=True, methods=['post'])
    def add_invite_link(self):
        # !TODO
        return Response()


InviteLinkViewSet = get_viewset(InviteLinkSerializer, InviteLink)
