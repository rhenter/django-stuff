from uuid import UUID

from django.db import models

from django_utils.fields import UUIDPrimaryKeyField
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer


class BaseModel(models.Model):
    class Meta:
        abstract = True


class SlugModel(BaseModel):
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=16)


class StatusModel(BaseModel):
    class Meta:
        abstract = True

    status = models.CharField(max_length=64)


class TimestampedModel(BaseModel):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at')
    )


class UUIDModel(BaseModel):
    class Meta:
        abstract = True

    id = UUIDPrimaryKeyField()


class SerializerModel(models.Model):
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

        # Turns our data JSON serializable:
        for key, value in data.items():
            if isinstance(value, UUID):
                data[key] = str(value)

        return data
