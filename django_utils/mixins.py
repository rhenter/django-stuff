from django.forms import ValidationError


class InvalidValuesFieldMixin:
    invalid_values = ()

    def clean(self, value):
        value = super().clean(value)
        if value in self.invalid_values:
            raise ValidationError(self.error_messages['invalid'])
        return value
