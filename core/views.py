from core.mixins import DetailedListViewSetMixin
from core import serializers, filters, models


# Create your views here.


class PersonViewSet(DetailedListViewSetMixin):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    serializer_action_classes = {
        "detailed": serializers.PersonDetailedSerializer,
        "detailed_list": serializers.PersonDetailedSerializer,
    }
    filterset_class = filters.PersonFilter
    ordering_fields = ()
