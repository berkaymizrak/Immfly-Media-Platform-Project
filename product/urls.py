from django.urls import path
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r'groups', views.GroupsViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'channels', views.ChannelViewSet)
router.register(r'content', views.ContentViewSet)

urlpatterns = [
]
