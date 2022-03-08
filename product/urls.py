from django.urls import path
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r"groups", views.GroupsViewSet)

urlpatterns = [
]
