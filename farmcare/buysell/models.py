from django.db import models
# from typing_extensions import Required
from django.contrib.auth.models import User


class Form(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=255, null=False)
    phone_no = models.BigIntegerField(null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    crop_name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=False)
    
class MandiDetails(models.Model):
    state = models.CharField(max_length=255, null=False,default='')
    district = models.CharField(max_length=255, null=False,default='')
    market = models.CharField(max_length=255, null=False,default='')
    commodity = models.CharField(max_length=255, null=False,default='')
    variety= models.CharField(max_length=255, null=False,default='')
    grade = models.CharField(max_length=255, null=False,default='')
    arrival_date = models.CharField(max_length=255, null=False,default='')
    min_price = models.CharField(max_length=255, null=False,default='')
    max_price = models.CharField(max_length=255, null=False,default='')
    modal_price = models.CharField(max_length=255, null=False,default='')

