from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    EmailField,
    BooleanField,
    DateTimeField,
    SerializerMethodField,
)
from cabinet.models import (
    Description,
    Title,
    ReleaseDate,
    Cabinet,
    Genre,
)


class ReleaseDateSerializer(ModelSerializer):
    """ReleaseDate serializer."""

    published = CharField(required=True)
    date = DateTimeField(read_only=True)

    class Meta:
        model = ReleaseDate
        fields = (
            'published',
            'date',
        )


class TitleSerializer(ModelSerializer):
    """Title serializer."""

    name = CharField(required=True)
    link = CharField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'name',
            'link',
        )


class DescriptionSerializer(ModelSerializer):
    """Description serializer."""

    text_en = CharField(read_only=True)
    text_ru = CharField(read_only=True)

    class Meta:
        model = Description
        fields = (
            'text_en',
            'text_ru',
        )


class CabinetSerializer(ModelSerializer):
    """Cabinet serializer."""

    id = IntegerField(read_only=True)
    studio = CharField()
    rating = IntegerField()

    release_date = ReleaseDateSerializer(
        required=True
    )
    title = TitleSerializer(
        required=True
    )
    description = DescriptionSerializer(
        required=True
    )
    datetime_created = DateTimeField(read_only=True)
    datetime_updated = DateTimeField(read_only=True)
    datetime_deleted = DateTimeField(read_only=True)

    name = SerializerMethodField(
        method_name='get_name'
    )

    class Meta:
        model = Cabinet
        fields = (
            'id',
            'studio',
            'rating',
            'release_date',
            'title',
            'description',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
            'name',
        )

    def get_name(self, obj: Cabinet) -> int:
        return f'{obj.studio} | {obj.title.name}'
