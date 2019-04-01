from django.db import models

class BillDetails(models.Model):
    billNo = models.IntegerField()
    billDate = models.CharField(max_length=100)
    shopId = models.IntegerField()    
    itemName = models.CharField(max_length=1000)
    itemRate = models.CharField(max_length=100)
    itemHsnCode = models.CharField(max_length=20)
    itemQuantity = models.IntegerField()
    itemMrp = models.CharField(max_length=100)
    itemGst = models.CharField(max_length=10)
    itemScheme = models.CharField(max_length=10)    
    itemTotal = models.CharField(max_length=100)

class Transactions(models.Model):
    billNo = models.IntegerField()
    shopId = models.IntegerField()
    date = models.CharField(max_length=100)
    total = models.CharField(max_length=100)