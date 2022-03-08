from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    verbose_name = _('Products')

    def ready(self):
        from media_platform.router import router as main_router

        from .urls import router

        main_router.extend(router)
