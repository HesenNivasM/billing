from django.db import models

class Shops(models.Model):
    name = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    gstNo = models.CharField(max_length=200, null=True, blank=True, default=None)
    areaCode = models.IntegerField()
    address = models.CharField(max_length=2500)
    phoneNo = models.CharField(max_length=10)
    balance = models.CharField(max_length=100,default = "0")

    def __str__(self):
        return str(self.name)
