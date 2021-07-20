from django.db import models

from common.models import BaseModel


class Todo(BaseModel):
    description = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
