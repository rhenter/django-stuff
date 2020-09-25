from django.db import models
from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone


class SignalsManager(models.Manager):

    def create(self, **kwargs):
        model_instance = self.initialize_model_instance(**kwargs)
        with transaction.atomic():
            model_instance.save()
        return model_instance

    def initialize_model_instance(self, **kwargs):
        return self.model(**kwargs)


class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now(), is_deleted=True)

    def hard_delete(self):
        return super().delete()

    def restore(self):
        return super().update(deleted_at=None, is_deleted=False)

    def trash(self):
        return self.filter(is_deleted=True)


class SoftDeleteManager(SignalsManager):
    def __init__(self, *args, **kwargs):
        self.show_deleted = kwargs.pop('show_deleted', False)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.show_deleted:
            return SoftDeleteQuerySet(self.model, using=self._db)
        return SoftDeleteQuerySet(self.model, using=self._db).exclude(is_deleted=True)

    def delete(self):
        return self.get_queryset().delete()

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def restore(self):
        return self.get_queryset().restore()

    def filter(self, *args, **kwargs):
        if 'is_deleted' in kwargs:
            qs = SoftDeleteQuerySet(self.model, using=self._db)
            return qs.filter(*args, **kwargs)
        return super().filter(*args, **kwargs)
