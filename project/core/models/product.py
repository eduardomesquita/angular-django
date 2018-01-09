from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'product'
