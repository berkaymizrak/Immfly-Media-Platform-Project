from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from product import models


class GroupsFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Groups
        fields = (
            "name",
            "name_autocomplete",
            "code",
        )

