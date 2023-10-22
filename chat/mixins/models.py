from django.conf import settings
from django.db import models

from common.mixins.models import TitleInfoMixin


class CommunityInfoMixin(TitleInfoMixin):
    slug = models.SlugField(default=None, null=True)
    messages = models.ManyToManyField(to='chat.Message', blank=True)
    admins = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='%(class)s_admins')
    members = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='%(class)s_members')
    private = models.BooleanField(default=False)
    invite_links = models.ManyToManyField(to='chat.InviteLink', blank=True)

    class Meta:
        abstract = True
