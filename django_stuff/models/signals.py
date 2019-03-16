import inspect

from django.db import transaction

from .generic import SerializerModel
from .managers import SignalsManager


class SignalsModel(SerializerModel):

    class Meta:
        abstract = True

    objects = SignalsManager()

    def get_context(self, **kwargs):
        force_insert = kwargs.get('force_insert', False)
        creation_conditions = (
            self.id is None,
            force_insert is True
        )
        context = {'is_creation': any(creation_conditions)}
        context.update(kwargs)
        return context

    def trigger_event(self, event_name, context):
        for attribute in dir(self):
            if attribute.startswith(event_name):
                method = getattr(self, attribute)
                if inspect.ismethod(method):
                    method(context)

    def save(self, *args, **kwargs):
        force_insert = kwargs.get('force_insert', False)
        context = self.get_context(force_insert=force_insert)

        if context['is_creation']:
            super().save(*args, **kwargs)
        else:
            with transaction.atomic():
                self.trigger_event('pre_save', context)
                super().save(*args, **kwargs)
                self.trigger_event('post_save', context)

    def delete(self, *args, **kwargs):
        context = self.get_context()

        with transaction.atomic():
            self.trigger_event('pre_delete', context)
            super().delete(*args, **kwargs)
            self.trigger_event('post_delete', context)
