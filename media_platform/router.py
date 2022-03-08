from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    def extend(self, external_router):
        self.registry.extend(external_router.registry)


router = DefaultRouter()
