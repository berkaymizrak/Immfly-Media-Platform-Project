from core import services
from django.http import HttpResponse
from openpyxl.writer.excel import save_virtual_workbook
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


class ExportViewSetMixin(viewsets.ModelViewSet):
    @action(detail=False, methods=["get"])
    def export(self, request, *args, **kwargs):
        excel_type = request.GET.get('excel_type', 'csv')
        qs = self.filter_queryset(self.get_queryset())
        serializer_class = self.get_serializer_class()
        service = services.ExcelExportService(
            queryset=qs, serializer_class=serializer_class,
        )
        if excel_type == 'xlsx':
            wb = service.create_workbook()
            filename = service.generate_file_name('xlsx')
            response = HttpResponse(
                save_virtual_workbook(wb), content_type="application/vnd.ms-excel"
            )
            response["Content-Disposition"] = f'attachment; filename="{filename}"'
        else:  # csv
            response = service.create_csv(True)
        return response
