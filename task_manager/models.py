from django.conf import settings
from django.db import models

from common.mixins.models import TitleInfoMixin
from task_manager.utils.models import do_from_today, do_to_today


class Period(models.Model):
    every_day = models.BooleanField(default=False)
    every_days = models.BooleanField(default=False)
    every_calendar_month = models.BooleanField(default=False)
    cont_per_period = models.PositiveSmallIntegerField(default=1)
    all_day = models.BooleanField(default=True)


class Task(TitleInfoMixin):
    do_from = models.DateTimeField(default=do_from_today)
    do_to = models.DateTimeField(default=do_to_today)
    is_done = models.BooleanField(default=False)
    subtasks = models.ManyToManyField(to='self', blank=True)
    for_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                 default=None, null=True)
    period = models.ForeignKey(to=Period, on_delete=models.SET_NULL, default=None, null=True)


class Team(TitleInfoMixin):
    members = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)


class Table(TitleInfoMixin):
    tasks = models.ManyToManyField(to=Task, blank=True)


class Project(TitleInfoMixin):
    tasks = models.ManyToManyField(to=Task, blank=True)
    tables = models.ManyToManyField(to=Table, blank=True)
    team = models.ManyToManyField(to=Team)
