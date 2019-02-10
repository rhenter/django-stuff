import uuid

from django.core.validators import RegexValidator
from django.db import models
from localflavor.br.forms import BRCNPJField, BRCPFField

from .mixins import InvalidValuesFieldMixin


class UUIDPrimaryKeyField(models.UUIDField):

    def __init__(self, *args, **kwargs):
        kwargs['primary_key'] = True
        kwargs['unique'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)

        if value is None:
            value = uuid.uuid4()
            setattr(model_instance, self.attname, value)

        return value


class CPFField(InvalidValuesFieldMixin, BRCPFField):
    invalid_values = ('00000000191',)


class CNPJField(InvalidValuesFieldMixin, BRCNPJField):
    invalid_values = ('00000000000000', '22222222000191', '33333333000191', '44444444000191',
                      '55555555000191', '66666666000191', '77777777000191', '88888888000191',
                      '99999999000191')


class CharFieldDigitsOnly(models.CharField):
    default_validators = [RegexValidator(r'^([\s\d]+)$', 'Only digits characters')]
