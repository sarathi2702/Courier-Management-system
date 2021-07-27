from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    consignment_id = models.IntegerField()
    order_date = models.DateTimeField(default=timezone.now)
    weight = models.FloatField()
    destination = models.CharField(max_length=20)
    amount = models.FloatField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.destination