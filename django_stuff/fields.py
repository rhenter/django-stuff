import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ValidationError
from localflavor.br.forms import BRCNPJField, BRCPFField


class InvalidValuesField:
    invalid_values = ()

    def clean(self, value):
        value = super().clean(value)
        if value in self.invalid_values:
            raise ValidationError(self.error_messages['invalid'])
        return value


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


class CPFField(InvalidValuesField, BRCPFField):
    invalid_values = ('00000000191',)


class CNPJField(InvalidValuesField, BRCNPJField):
    invalid_values = ('00000000000000', '22222222000191', '33333333000191', '44444444000191',
                      '55555555000191', '66666666000191', '77777777000191', '88888888000191',
                      '99999999000191')


class CharFieldDigitsOnly(models.CharField):
    default_validators = [RegexValidator(r'^([\s\d]+)$', 'Only digits characters')]
