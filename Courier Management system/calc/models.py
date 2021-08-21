from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Orders(models.Model):
    consignment_id = models.IntegerField(primary_key='consignment_id',auto_created=True)
    order_date = models.DateTimeField(default=timezone.now)
    weight = models.FloatField()
    from_place = models.CharField(max_length=20,null=True)
    destination = models.CharField(max_length=20)
    amount = models.FloatField(weight,null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.destination

    def get_absolute_url(self):
        return reverse('about')

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)