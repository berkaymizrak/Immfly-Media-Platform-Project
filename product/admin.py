from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from product import models

# Register your models here.


@admin.register(models.Groups)
class GroupsAdmin(ImportExportModelAdmin):

    list_display = [
        'name',
        'code',
    ]
    search_fields = [
        'name',
        'code',
    ]


@admin.register(models.Genre)
class GenreAdmin(ImportExportModelAdmin):

    list_display = [
        'name',
        'age_rate',
    ]
    search_fields = [
        'name',
    ]


@admin.register(models.Channel)
class ChannelAdmin(ImportExportModelAdmin):

    list_display = [
        'title',
        'parent',
        'language',
        'code',
    ]
    search_fields = [
        'title',
    ]
    list_filter = [
        'group',
    ]


@admin.register(models.Content)
class ContentAdmin(ImportExportModelAdmin):

    list_display = [
        'name',
        'description',
        'season',
        'episode',
        'rating',
        'channel',
    ]
    search_fields = [
        'name',
        'description',
    ]
    list_filter = [
        'genre',
    ]

