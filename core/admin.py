from core import models
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(models.Person)
class PersonAdmin(ImportExportModelAdmin):

    list_display = [
        'id',
        'first_name',
        'last_name',
        'date_of_birth',
    ]
    search_fields = [
        'first_name',
        'last_name',
    ]
    list_editable = [
        'first_name',
        'last_name',
        'date_of_birth',
    ]


@admin.register(models.Document)
class DocumentAdmin(ImportExportModelAdmin):

    list_display = [
        'id',
        'document',
        'doc_type',
    ]
    list_filter = [
        'doc_type',
    ]
    list_editable = [
        'doc_type',
    ]


@admin.register(models.Language)
class LanguageAdmin(ImportExportModelAdmin):

    list_display = [
        'name',
        'code',
    ]
    search_fields = [
        'name',
        'code',
    ]


