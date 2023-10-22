import uuid
from django.db import models

from common.mixins.models import InfoMixin
from chat.mixins.models import CommunityInfoMixin


class Message(InfoMixin):
    text = models.TextField()


class Group(CommunityInfoMixin):
    ...


class Channel(CommunityInfoMixin):
    ...


class InviteLink(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
