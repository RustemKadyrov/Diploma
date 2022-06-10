from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
)
from django.dispatch import receiver
from django.db.models.base import ModelBase

from abstracts.utils import send_email
from cabinet.models import Cabinet


@receiver(
    post_save,
    sender=Cabinet
)
def post_save_cabinet(
    sender: ModelBase,
    instance: Cabinet,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal post-save Cabinet."""

    # Sending Email to User linked to Cabinet as uploader
    #
    send_email(
        'DJANGO_SUBJECT',
        'DJANGO_TEXT',
        'Rustem825@gmail.com'
    )


@receiver(
    pre_save,
    sender=Cabinet
)
def pre_save_cabinet(
    sender: ModelBase,
    instance: Cabinet,
    **kwargs: dict
) -> None:
    """Signal pre-save Cabinet."""
    pass

    # instance.save()


@receiver(
    post_delete,
    sender=Cabinet
)
def post_delete_cabinet(
    sender: ModelBase,
    instance: Cabinet,
    **kwargs: dict
) -> None:
    """Signal post-delete Cabinet."""

    instance.delete()


@receiver(
    pre_delete,
    sender=Cabinet
)
def pre_delete_cabinet(
    sender: ModelBase,
    instance: Cabinet,
    **kwargs: dict
) -> None:
    """Signal pre-delete Cabinet."""

    instance.delete()
