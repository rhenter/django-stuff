from uuid import UUID

from django.db import models

from django_stuff.fields import UUIDPrimaryKeyField
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer


class BaseModel(models.Model):

    class Meta:
        abstract = True


class SlugModel(BaseModel):
    slug = models.SlugField(max_length=16)

    class Meta:
        abstract = True


class TimestampedModel(BaseModel):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at')
    )

    class Meta:
        abstract = True


class UUIDModel(BaseModel):
    id = UUIDPrimaryKeyField()

    class Meta:
        abstract = True


class SerializerModel(BaseModel):

    class Meta:
        abstract = True

    @cached_property
    def serializer(self):
        class SelfSerializer(ModelSerializer):

            class Meta:
                pass

        SelfSerializer.Meta.model = self
        SelfSerializer.Meta.fields = '__all__'
        return SelfSerializer

    def serialize(self):
        data = self.serializer(self).data

        for key, value in data.items():
            if isinstance(value, UUID):
                data[key] = str(value)
        return data
