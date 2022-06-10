from datetime import datetime

from django.db.models import (
    Model,
    QuerySet,
    ManyToManyField,
    ForeignKey,
    OneToOneField,
    CharField,
    TextField,
    IntegerField,
    DateTimeField,
    PROTECT,
    CASCADE,
)
from abstracts.models import AbstractDateTime
from abstracts.validators import AbstractValidator


class Title(Model):
    """Title entity."""

    name = CharField(
        verbose_name='имя',
        max_length=50
    )
    link = TextField(
        verbose_name='ссылка'
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'дата выпуска'
        verbose_name_plural = 'даты выпуска'

    def __str__(self) -> str:
        return f'Тайтл: {self.name}'


class ReleaseDate(Model):
    """ReleaseDate entity."""

    published = CharField(
        verbose_name='выпущен',
        max_length=20
    )
    date = DateTimeField(
        verbose_name='дата'
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'дата выпуска '
        verbose_name_plural = 'даты выпуска '

    def __str__(self) -> str:
        return f'Дата выпуска: {self.published}'


class CabinetQuerySet(QuerySet):
    """Cabinet queryset."""

    def get_deleted(self) -> QuerySet['Cabinet']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['Cabinet']:
        return self.filter(
            datetime_deleted__isnull=True
        )


class Cabinet(AbstractDateTime, AbstractValidator):
    """Cabinet entity."""

    studio = CharField(
        verbose_name='Категория',
        max_length=100,
        default=''
    )
    rating = IntegerField(
        verbose_name='Индентификатор',
    )
    release_date = ForeignKey(
        ReleaseDate,
        on_delete=PROTECT,
        verbose_name='дата утверждения'
    )
    title = OneToOneField(
        Title,
        on_delete=CASCADE,
        verbose_name='Название',
        null=True, blank=True
    )
    objects = CabinetQuerySet().as_manager()

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self) -> str:
        return f'{self.studio} | {self.title.name}, {self.rating}'

    def clean(self) -> None:
        self.validate_release_date(
            self.release_date.date
        )

    def save(self, *args: tuple, **kwargs: dict) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_field=['datetime_deleted']
        )
        # super().delete()


class Description(Model):
    """Description entity."""

    cabinet = OneToOneField(
        Cabinet,
        on_delete=CASCADE,
        verbose_name='Заявка',
        null=True, blank=True
    )
    text_en = TextField(
        verbose_name='текст на английском',
        default=''
    )
    text_ru = TextField(
        verbose_name='текст на русском',
        default=''
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'описание'
        verbose_name_plural = 'описания'

    def __str__(self) -> str:
        return 'Описание документа'


class Genre(Model):
    """Genre entity."""

    name = CharField(
        verbose_name='Название',
        max_length=50
    )
    cabinet = ManyToManyField(
        Cabinet,
        related_name='genres',
        verbose_name='документы'
    )

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    def __str__(self) -> str:
        return f'Документ: {self.name}'
