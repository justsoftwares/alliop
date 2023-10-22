from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    def get_default_basename(self, viewset):
        return viewset.serializer_class.Meta.model
