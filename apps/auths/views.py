from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.validators import APIValidator
from abstracts.mixins import JsonResponseMixin
from auths.models import CustomUser
from auths.serializers import CustomUserSerializer


class CustomUserViewSet(JsonResponseMixin, ViewSet):
    """ViewSet for CustomUser."""

    permission_classes: tuple = (
        permissions.AllowAny,
    )
    queryset: QuerySet[CustomUser] = \
        CustomUser.objects.get_not_deleted()

    def get_queryset(self) -> QuerySet[CustomUser]:
        return self.queryset.filter(
            is_superuser=False
        )

    @action(
        methods=['post'],
        detail=False,
        url_path='my-custom-endpoint',
        permission_classes=(
            permissions.AllowAny,
        )
    )
    def my_custom_endpoint(
        self,
        request: DRF_Request
    ) -> DRF_Response:
        """Handles POST-request to show custom-info about custom_users."""

        data: list = [
            user.id for user in self.get_queryset()
        ]
        return self.get_json_response(
            data
        )

    def list(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to show custom_users."""

        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                self.get_queryset(),
                many=True
            )
        return self.get_json_response(
            serializer.data
        )

    def create(self, request: DRF_Request) -> DRF_Response:
        """Handles POST-request to show custom_users."""

        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                data=request.data
            )
        if serializer.is_valid():

            serializer.save()

            return self.get_json_response(
                f'Объект {serializer.id} создан'
            )
        return self.get_json_response(
            'Объект не создан'
        )

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles GET-request with ID to show custom_user."""

        # Retrieving certain object
        #
        custom_user: Optional[CustomUser] = None
        try:
            custom_user = self.get_queryset().get(
                id=pk
            )
        except CustomUser.DoesNotExist:
            return self.get_json_response(
                'Не нашел такого юзера'
            )
        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                custom_user
            )
        return self.get_json_response(
            serializer.data
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: int = 0
    ) -> DRF_Response:
        """Handles PATCH-request with ID to show custom_user."""

        raise APIValidator(
            '\'PATCH\' метод не имплементирован',
            'warning',
            '403'
        )

    def update(self, request: DRF_Request) -> DRF_Response:
        """Handles PUT-request with ID to show custom_user."""

        raise APIValidator(
            '\'PUT\' метод не имплементирован',
            'warning',
            '403'
        )

    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles DELETE-request with ID to show custom_user."""

        custom_user: Optional[CustomUser] = None
        try:
            custom_user = self.get_queryset().get(
                id=pk
            )
        except CustomUser.DoesNotExist:
            return self.get_json_response(
                f'Объект с ID: {pk} не найден'
            )

        custom_user.datetime_deleted = datetime.now()
        custom_user.save(
            update_fields=['datetime_deleted']
        )
        return self.get_json_response(
            f'Объект {custom_user.id} удален'
        )
