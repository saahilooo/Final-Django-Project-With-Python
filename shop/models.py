from django.db import models


# Create your models here.

class Shop(models.Model):
    itemname = models.CharField(max_length=200)
    peritemprice = models.CharField(max_length=200)
    totalqty = models.CharField(max_length=200)
    totalprice = models.CharField(max_length=200)


class Meta:
    db_table = "shop"
