from django.db import models
from .client import Client
from .product import Product
import datetime


class Sales(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)

    client = models.ForeignKey(Client, null=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'sales'
