from core.mixins import DetailedListViewSetMixin
from product import serializers, filters, models


# Create your views here.


class GroupsViewSet(DetailedListViewSetMixin):
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupsSerializer
    serializer_action_classes = {
        "detailed": serializers.GroupsDetailedSerializer,
        "detailed_list": serializers.GroupsDetailedSerializer,
    }
    filterset_class = filters.GroupsFilter
    ordering_fields = ()
