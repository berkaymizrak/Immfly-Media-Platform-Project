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


class DocumentViewSet(DetailedListViewSetMixin):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    serializer_action_classes = {
        "detailed": serializers.DocumentDetailedSerializer,
        "detailed_list": serializers.DocumentDetailedSerializer,
    }
    filterset_class = filters.DocumentFilter
    ordering_fields = ()


class LanguageViewSet(DetailedListViewSetMixin):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    serializer_action_classes = {
        "detailed": serializers.LanguageDetailedSerializer,
        "detailed_list": serializers.LanguageDetailedSerializer,
    }
    filterset_class = filters.LanguageFilter
    ordering_fields = ()
