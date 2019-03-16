from django.db import models
from django.db import transaction


class SignalsManager(models.Manager):

    def create(self, **kwargs):
        model_instance = self.initialize_model_instance(**kwargs)
        with transaction.atomic():
            model_instance.trigger_event('pre_save', {'is_creation': True})
            model_instance.save()
            model_instance.trigger_event('post_save', {'is_creation': False})
        return model_instance

    def initialize_model_instance(self, **kwargs):
        return self.model(**kwargs)
