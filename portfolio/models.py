from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHARITY_TYPE = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)

class Category(models.Model):
    name = models.CharField(max_length=64)

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    type = models.IntegerField(choices=CHARITY_TYPE, default=1)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField(default=1)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=24)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)