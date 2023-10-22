from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class InfoMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None,
                              null=True, related_name='%(class)s_owner', editable=False)

    class Meta:
        abstract = True

    def get_owned_objects(self, owner_id: int):
        return self.__class__.objects.filter(owner=owner_id)


@receiver(pre_save, sender=InfoMixin)
def set_owner_on_save(sender, instance, **kwargs):
    if not instance.owner:
        instance.owner = instance.owner or getattr(instance, '_request_user_id', None)


class TitleInfoMixin(InfoMixin):
    title = models.CharField(max_length=100, default='', blank=True)

    tags = models.CharField(max_length=100, default=None, null=True)

    class Meta:
        abstract = True
