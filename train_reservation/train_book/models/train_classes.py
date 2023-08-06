
from django.db import models
from .train_cabins import TrainCabin
import uuid

# Create your models here.
class TrainCabinClass(models.Model):
    train_cabin_class_id = models.CharField(max_length=3,primary_key=True)
    cabin_class_name = models.CharField(max_length=100)
    fair_price = models.IntegerField()
    train_cabins = models.ManyToManyField(TrainCabin, null=True, related_name="train_cabins")
