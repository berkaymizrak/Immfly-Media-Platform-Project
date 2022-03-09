from core.mixins import DetailedListViewSetMixin, ExportViewSetMixin
from product import serializers, filters, models


# Create your views here.


class GroupsViewSet(DetailedListViewSetMixin):
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupsSerializer
    serializer_action_classes = {
        'detailed': serializers.GroupsDetailedSerializer,
        'detailed_list': serializers.GroupsDetailedSerializer,
    }
    filterset_class = filters.GroupsFilter
    ordering_fields = ()


class GenreViewSet(DetailedListViewSetMixin):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    serializer_action_classes = {
        'detailed': serializers.GenreDetailedSerializer,
        'detailed_list': serializers.GenreDetailedSerializer,
    }
    filterset_class = filters.GenreFilter
    ordering_fields = ()


class ChannelViewSet(DetailedListViewSetMixin, ExportViewSetMixin):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    serializer_action_classes = {
        'detailed': serializers.ChannelDetailedSerializer,
        'detailed_list': serializers.ChannelDetailedSerializer,
        'export': serializers.ChannelExportSerializer,
    }
    filterset_class = filters.ChannelFilter
    ordering_fields = ()


class ContentViewSet(DetailedListViewSetMixin):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
    serializer_action_classes = {
        'detailed': serializers.ContentDetailedSerializer,
        'detailed_list': serializers.ContentDetailedSerializer,
    }
    filterset_class = filters.ContentFilter
    ordering_fields = ()
