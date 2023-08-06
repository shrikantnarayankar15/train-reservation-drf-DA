from django.db import models
import uuid
from .train_cabins import TrainCabin
# Create your models here.
class Train(models.Model):
    train_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=100)
    src = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    train_cabins = models.ManyToManyField(TrainCabin, null=True, related_name="trains")
