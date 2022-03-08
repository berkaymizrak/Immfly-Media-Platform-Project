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


class ChannelGroupInline(admin.TabularInline):
    model = models.Channel.group.through
    autocomplete_fields = ('groups', )
    extra = 0


@admin.register(models.Channel)
class ChannelAdmin(ImportExportModelAdmin):
    autocomplete_fields = (
        'parent',
        'language',
    )
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
    exclude = (
        'group',
    )
    inlines = [
        ChannelGroupInline,
    ]


class ContentGenreInline(admin.TabularInline):
    model = models.Content.genre.through
    autocomplete_fields = ('genre', )
    extra = 0


class ContentFileInline(admin.TabularInline):
    model = models.Content.file.through
    autocomplete_fields = ('document', )
    extra = 0


class ContentPersonInline(admin.TabularInline):
    model = models.Content.person.through
    autocomplete_fields = ('person', )
    extra = 0


@admin.register(models.Content)
class ContentAdmin(ImportExportModelAdmin):
    autocomplete_fields = (
        'channel',
    )
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
    exclude = (
        'genre',
        'file',
    )
    inlines = [
        ContentGenreInline,
        ContentFileInline,
        ContentPersonInline,
    ]
