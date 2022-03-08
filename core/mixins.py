from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class DetailedListViewSetMixin(viewsets.ModelViewSet):
    serializer_action_classes = {}
    ordering = ('id',)

    def get_serializer_class(self):
        """
        A class which inhertis this mixins should have variable
        `serializer_action_classes`.
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:
        class SampleViewSet(viewsets.ViewSet):
            serializer_class = DocumentSerializer
            serializer_action_classes = {
               'upload': UploadDocumentSerializer,
               'download': DownloadDocumentSerializer,
            }
            @action
            def upload:
                ...
        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    @action(detail=False, methods=['get'])
    def detailed_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        kwargs.update({'many': True, 'context': {'request': self.request}})
        if page is not None:
            serializer = self.get_serializer_class()(page, **kwargs)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer_class()(queryset, **kwargs)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def detailed(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs.pop('pk')
        kwargs.update({'context': {'request': self.request}})
        serializer = self.get_serializer_class()(instance, **kwargs)
        return Response(serializer.data)
