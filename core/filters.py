from django_filters.rest_framework import DjangoFilterBackend


class CustomFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        qs = super().filter_queryset(request, queryset, view)
        return qs
