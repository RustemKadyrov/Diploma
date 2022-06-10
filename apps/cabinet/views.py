from typing import Optional
from datetime import datetime

from rest_framework.permissions import (
    AllowAny,
    # IsAuthenticated,
)
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.validators import APIValidator
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
from abstracts.mixins import JsonResponseMixin
from cabinet.models import Cabinet
from cabinet.serializers import (
    CabinetSerializer,
)
from cabinet.permissions import (
    CabinetPermission,
)


class CabinetViewSet(JsonResponseMixin, ViewSet):
    """ViewSet for Cabinet."""

    permission_classes: tuple = (
        CabinetPermission,
    )
    queryset: QuerySet[Cabinet] = \
        Cabinet.objects.get_not_deleted()

    serializer_class: CabinetSerializer = \
        CabinetSerializer

    pagination_class: AbstractPageNumberPaginator = \
        AbstractPageNumberPaginator

    def get_queryset(self) -> QuerySet[Cabinet]:
        return self.queryset.select_related(
            'title',
            'release_date',
            'description',
        )

    @action(
        methods=['get'],
        detail=False,
        url_path='list-2',
        permission_classes=(
            AllowAny,
        )
    )
    def list_2(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to list Cabinet."""

        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: CabinetSerializer = \
            self.serializer_class(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )

    def list(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to list Cabinet."""

        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: CabinetSerializer = \
            self.serializer_class(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )

    def create(self, request: DRF_Request) -> DRF_Response:
        """Handles POST-request to show custom_users."""
        ...

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles GET-request with ID to show custom_user."""

        raise APIValidator(
            '\'GET\' метод не имплементирован',
            'warning',
            '403'
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: int = 0
    ) -> DRF_Response:
        """Handles PATCH-request with ID to show custom_user."""
        ...

    def update(self, request: DRF_Request) -> DRF_Response:
        """Handles PUT-request with ID to show custom_user."""
        ...

    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles DELETE-request with ID to show custom_user."""
        ...
