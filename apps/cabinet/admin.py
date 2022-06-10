from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from cabinet.models import (
    Description,
    Title,
    ReleaseDate,
    Cabinet,
    Genre,
)


class ReleaseDateAdmin(admin.ModelAdmin):

    readonly_fields = (
        'published',
        'date',
    )


class DescriptionAdmin(admin.ModelAdmin):

    readonly_fields = ()


class TitleAdmin(admin.ModelAdmin):

    readonly_fields = ()


class CabinetAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


class GenreAdmin(admin.ModelAdmin):

    readonly_fields = ()


admin.site.register(
    ReleaseDate, ReleaseDateAdmin
)
admin.site.register(
    Description, DescriptionAdmin
)
admin.site.register(
    Title, TitleAdmin
)
admin.site.register(
    Cabinet, CabinetAdmin
)
admin.site.register(
    Genre, GenreAdmin
)
