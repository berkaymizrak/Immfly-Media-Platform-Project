from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from product import models

class GroupsFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = models.Groups
        fields = (
            'name',
            'name_autocomplete',
            'code',
        )


class GenreFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = models.Genre
        fields = (
            'name',
            'name_autocomplete',
            'age_rate',
        )


class ChannelFilter(filters.FilterSet):
    parent_code = filters.CharFilter(
        field_name='parent__code',
    )
    having_parent = filters.Filter(
        field_name='parent',
        method='filter_having_parent',
        label=_('Having Parent'),
    )
    title_autocomplete = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )
    group_name = filters.CharFilter(
        field_name='group__name',
    )
    group_name_autocomplete = filters.CharFilter(
        field_name='group__name',
        lookup_expr='icontains',
    )
    group_code = filters.CharFilter(
        field_name='group__code',
    )
    group_code_autocomplete = filters.CharFilter(
        field_name='group__code',
        lookup_expr='icontains',
    )
    search = filters.CharFilter(
        lookup_expr='icontains',
        method='filter_search',
        label=_('Search in Code and Name'),
    )

    class Meta:
        model = models.Channel
        fields = (
            'parent',
            'parent_code',
            'having_parent',
            'title',
            'title_autocomplete',
            'group',
            'group_name',
            'group_name_autocomplete',
            'group_code',
            'group_code_autocomplete',
            'search',
        )

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(group__code__icontains=value) | Q(group__name__icontains=value)
        )

    def filter_having_parent(self, queryset, name, value):
        if value.lower() in ['none', '0', ]:
            value = None
        return queryset.filter(parent=value)


class ContentFilter(filters.FilterSet):
    name_autocomplete = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = models.Content
        fields = (
            'name',
            'name_autocomplete',
        )
