from django_filters import rest_framework as filters
from core import models


class PersonFilter(filters.FilterSet):
    first_name_autocomplete = filters.CharFilter(
        field_name="first_name",
        lookup_expr="icontains",
    )
    last_name_autocomplete = filters.CharFilter(
        field_name="last_name",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Person
        fields = (
            "first_name",
            "first_name_autocomplete",
            "last_name",
            "last_name_autocomplete",
        )
