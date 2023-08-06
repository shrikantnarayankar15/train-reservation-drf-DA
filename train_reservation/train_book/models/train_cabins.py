
from django.db import models
# from .train_classes import TrainCabinClass
import uuid

# Create your models here.
class TrainCabin(models.Model):
    train_cabin_id = models.CharField(max_length=3,primary_key = True,)
    train_cabin_limit = models.IntegerField()