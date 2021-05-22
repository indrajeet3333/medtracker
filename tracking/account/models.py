from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_manufacturer     =   models.BooleanField(default=False)
    is_distributor      =   models.BooleanField(default=False)
    is_retailer         =   models.BooleanField(default=False)
    is_government_user  =   models.BooleanField(default=False)
    is_normal_user      =   models.BooleanField(default=False)
    first_name          =   models.CharField(max_length=100)
    last_name           =   models.CharField(max_length=100)

class Manufacturer(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    company_name        =   models.CharField(max_length=100)
    phone_no            =   models.CharField(max_length=15)
    cin_no              =   models.CharField(max_length=21)

class Distributor(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    agency_name         =   models.CharField(max_length=100)
    phone_no            =   models.CharField(max_length=15)
    cin_no              =   models.CharField(max_length=21)
    state_distribution  =   models.CharField(max_length=50)
    city_distribution   =   models.CharField(max_length=50)

class Retailer(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    shop_name           =   models.CharField(max_length=100)
    phone_no            =   models.CharField(max_length=15)
    shop_act_no         =   models.CharField(max_length=14)
    state               =   models.CharField(max_length=50)
    city                =   models.CharField(max_length=50)

class Government_Body(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    deptartment         =   models.CharField(max_length=100)

class Normal_User(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    middle_name         =   models.CharField(max_length=100)
    aadhar_no           =   models.CharField(max_length=15)
    state               =   models.CharField(max_length=50)
    city                =   models.CharField(max_length=50)