from django.urls import path
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r"person", views.PersonViewSet)
router.register(r"document", views.DocumentViewSet)

urlpatterns = [
]
