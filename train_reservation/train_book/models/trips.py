from django.db import models
import uuid

from .trains import Train
# Create your models here.
class Trip(models.Model):
    trip_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    date = models.DateField()
