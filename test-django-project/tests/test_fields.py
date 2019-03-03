import pytest

from django.forms import ValidationError
from django_stuff.fields import CNPJField, CPFField


pytestmark = pytest.mark.django_db


def test_cpf_field_valid():
    value = '21552411273'
    assert CPFField().clean(value) == value


@pytest.mark.parametrize('value', CPFField.invalid_values + ('12345678901',))
def test_cpf_field_invalid(value):
    with pytest.raises(ValidationError):
        CPFField().clean(value)


def test_cnpj_field_valid():
    value = '15370536000176'
    assert CNPJField().clean(value) == value


@pytest.mark.parametrize('value', CNPJField.invalid_values + ('12345678901234',))
def test_cnpj_field_invalid(value):
    with pytest.raises(ValidationError):
        CNPJField().clean(value)
