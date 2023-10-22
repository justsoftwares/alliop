from typing import Sequence, Container

from rest_framework import viewsets

from common.permissions import get_permission_class
from common.utils import get_queryset_for_user


def get_viewset(_serializer_class, _queryset=None, _show_user_fields: Container = (),
                _edit_user_fields: Container = ('owner',), _only_user_objects: bool = False):
    class ModelViewSet(viewsets.ModelViewSet):
        serializer_class = _serializer_class
        queryset = _queryset
        permission_classes = [get_permission_class(_show_user_fields, _edit_user_fields)]

        def get_queryset(self):
            if self.queryset is None:
                return get_queryset_for_user(self.serializer_class.Meta.model, self.request.user.id,
                                             _show_user_fields, _edit_user_fields, _only_user_objects)
            return self.queryset

    return ModelViewSet
