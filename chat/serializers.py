from common.serializers import get_serializer
from chat.models import Message, Group, Channel, InviteLink

MessageSerializer = get_serializer(Message)
GroupSerializer = get_serializer(Group)
ChannelSerializer = get_serializer(Channel)
InviteLinkSerializer = get_serializer(InviteLink)
