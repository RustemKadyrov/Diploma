from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.contrib.admin import SimpleListFilter
from django.db.models import QuerySet


class CommonStateFilter(SimpleListFilter):
    title: str = 'Состояние'
    parameter_name: str = 'pages'

    def lookups(
        self,
        request: WSGIRequest,
        model_admin: Any
    ) -> list:
        """Lookups for any entity with AbstractDateTime."""

        return [
            ('deleted', 'Удаленные'),
            ('not_deleted', 'Неудаленные'),
        ]

    def queryset(
        self,
        request: WSGIRequest,
        queryset: QuerySet
    ) -> QuerySet:
        """QuerySet."""

        if self.value() == 'deleted':
            return queryset.get_deleted()

        if self.value() == 'not_deleted':
            return queryset.get_not_deleted()
