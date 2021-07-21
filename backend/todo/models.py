from django.utils.timezone import now
from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError

from common.models import BaseModel


class TodoManager(models.Manager):

    def complete(self, id, user):
        try:
            todo = self.get_by_user(user).get(id=id)
            todo.status = True
            todo.completed_at = now()
            todo.save()
        except self.model.DoesNotExist:
            raise ValidationError(_('Not Found!'))

    def get_by_user(self, user):
        return self.get_queryset().filter(created_by=user)


class Todo(BaseModel):
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    objects = TodoManager()
