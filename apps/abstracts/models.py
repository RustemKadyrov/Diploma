from django.db.models import (
    Model,
    DateTimeField,
)


class AbstractDateTime(Model):
    """Abstract entity for logging by time."""

    datetime_created = DateTimeField(
        verbose_name='время создания',
        auto_now_add=True
    )
    datetime_updated = DateTimeField(
        verbose_name='время обновления',
        auto_now=True
    )
    datetime_deleted = DateTimeField(
        verbose_name='время удаления',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True