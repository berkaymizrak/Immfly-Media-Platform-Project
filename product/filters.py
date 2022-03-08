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


class GenreFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Genre
        fields = (
            "name",
            "name_autocomplete",
            "age_rate",
        )


class ChannelFilter(filters.FilterSet):
    title_autocomplete = filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Channel
        fields = (
            "title",
            "title_autocomplete",
        )


class ContentFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Content
        fields = (
            "name",
            "name_autocomplete",
        )
