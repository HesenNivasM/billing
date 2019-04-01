from django.db import models

class Stocks(models.Model):
    name = models.CharField(max_length=1000)
    stockCode = models.CharField(max_length=100)
    hsnCode = models.CharField(max_length=20)
    quantity = models.IntegerField()
    mrp = models.CharField(max_length=100)
    gst = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)
