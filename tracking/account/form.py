from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Manufacturer,Distributor,Retailer,Government_Body,Normal_User

class ManufacturerSignUpForm(UserCreationForm):
    first_name      =   forms.CharField(required=True)
    last_name       =   forms.CharField(required=True)
    company_name    =   forms.CharField(required=True)
    phone_no        =   forms.CharField(required=True)
    cin_no          =   forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model   =   User

    @transaction.atomic
    def save(self):
        user                        =   super().save(commit=False)
        user.is_manufacturer        =   True
        user.first_name             =   self.cleaned_data.get('first_name')
        user.last_name              =   self.cleaned_data.get('last_name')
        user.save()
        manufacturer                =   Manufacturer.objects.create(user=user)
        manufacturer.company_name   =   self.cleaned_data.get('company_name')
        manufacturer.phone_no       =   self.cleaned_data.get('phone_no')
        manufacturer.cin_no         =   self.cleaned_data.get('cin_no')
        manufacturer.save()
        return user

class DistributorSignUpForm(UserCreationForm):
    first_name          =   forms.CharField(required=True)
    last_name           =   forms.CharField(required=True)
    agency_name         =   forms.CharField(required=True)
    phone_no            =   forms.CharField(required=True)
    cin_no              =   forms.CharField(required=True)
    state_distributor   =   forms.CharField(required=True)
    city_distributor    =   forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model   =   User

    @transaction.atomic
    def save(self):
        user                            =   super().save(commit=False)
        user.is_distributor             =   True
        user.first_name                 =   self.cleaned_data.get('first_name')
        user.last_name                  =   self.cleaned_data.get('last_name')
        user.save()
        distributor                     =   Distributor.objects.create(user=user)
        distributor.agency_name         =   self.cleaned_data.get('agency_name')
        distributor.phone_no            =   self.cleaned_data.get('phone_no')
        distributor.cin_no              =   self.cleaned_data.get('cin_no')
        distributor.state_distributor   =   self.cleaned_data.get('state_distributor')
        distributor.city_distributor    =   self.cleaned_data.get('city_distributor')
        distributor.save()
        return user

class RetailerSignUpForm(UserCreationForm):
    first_name          =   forms.CharField(required=True)
    last_name           =   forms.CharField(required=True)
    shop_name           =   forms.CharField(required=True)
    phone_no            =   forms.CharField(required=True)
    shop_act_no         =   forms.CharField(required=True)
    state               =   forms.CharField(required=True)
    city                =   forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model   =   User

    @transaction.atomic
    def save(self):
        user                    =   super().save(commit=False)
        user.is_retailer        =   True
        user.first_name         =   self.cleaned_data.get('first_name')
        user.last_name          =   self.cleaned_data.get('last_name')
        user.save()
        retailer                =   Retailer.objects.create(user=user)
        retailer.shop_name      =   self.cleaned_data.get('shop_name')
        retailer.phone_no       =   self.cleaned_data.get('phone_no')
        retailer.shop_act_no    =   self.cleaned_data.get('shop_act_no')
        retailer.state          =   self.cleaned_data.get('state')
        retailer.city           =   self.cleaned_data.get('city')
        retailer.save()
        return user

class GovernmentBodySignUpForm(UserCreationForm):
    first_name          =   forms.CharField(required=True)
    last_name           =   forms.CharField(required=True)
    department          =   forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model   =   User

    @transaction.atomic
    def save(self):
        user                    =   super().save(commit=False)
        user.is_government_user =   True
        user.first_name         =   self.cleaned_data.get('first_name')
        user.last_name          =   self.cleaned_data.get('last_name')
        user.save()
        retailer                =   Retailer.objects.create(user=user)
        retailer.deptartment    =   self.cleaned_data.get('department')
        retailer.save()
        return user

class NormalUserSignUpForm(UserCreationForm):
    first_name          =   forms.CharField(required=True)
    last_name           =   forms.CharField(required=True)
    middle_name         =   forms.CharField(required=True)
    aadhar_no           =   forms.CharField(required=True)
    state               =   forms.CharField(required=True)
    city                =   forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model   =   User

    @transaction.atomic
    def save(self):
        user                        =   super().save(commit=False)
        user.is_normal_user         =   True
        user.first_name             =   self.cleaned_data.get('first_name')
        user.last_name              =   self.cleaned_data.get('last_name')
        user.save()
        normal_user                 =   Normal_User.objects.create(user=user)
        normal_user.middle_name     =   self.cleaned_data.get('middle_name')
        normal_user.aadhar_no       =   self.cleaned_data.get('aadhar_no')
        normal_user.state           =   self.cleaned_data.get('state')
        normal_user.city            =   self.cleaned_data.get('city')
        normal_user.save()
        return user