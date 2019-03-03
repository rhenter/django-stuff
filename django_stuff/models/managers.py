from django.db import models
from django.db import transaction


class SignalsManager(models.Manager):
    def create(self, **kwargs):
        model_instance = self.initialize_model_instance(**kwargs)
        with transaction.atomic():
            model_instance.trigger_event('pre_save', {'is_creation': True})
            self.perform_create(model_instance, **kwargs)
            model_instance.trigger_event('post_save', {'is_creation': True})
        return model_instance

    def initialize_model_instance(self, **kwargs):
        return self.model(**kwargs)

    def perform_create(self, model_instance, **kwargs):
        model_instance.save(force_insert=True, **kwargs)
