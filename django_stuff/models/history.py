from .signals import SignalsModel
from .exceptions import HistoryModelNotSetError


class HistoryModel(SignalsModel):
    history_model = None
    history_parent_field_name = 'parent'

    def __init__(self, *args, **kwargs):
        if not self.history_model:
            raise HistoryModelNotSetError(
                "You should set the history_model attribute of {}".format(type(self).__name__)
            )

        super().__init__(*args, **kwargs)

    def save_history(self):
        data = {self.history_parent_field_name: self}

        history_model_fields = tuple(field.name for field in self.history_model._meta.fields)

        for field in self._meta.fields:
            name = field.name

            if name in ('id', 'created_at', 'updated_at'):
                continue

            if name in history_model_fields:
                value = getattr(self, name)
                data[field.name] = value

        self.history_model.objects.create(**data)

    def post_save_history(self, context):
        self.save_history()
