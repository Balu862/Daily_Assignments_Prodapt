from django.db import models
from datetime import datetime

from django.db.models.query_utils import check_rel_lookup_compatibility
# Create your models here.
class RegisterModel(models.Model):
    cname=models.CharField(max_length=50)
    profilephoto=models.ImageField(upload_to='images/',default=None)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    device=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    aadhar=models.BigIntegerField()
    aadharphoto = models.ImageField(upload_to='images/',default=None)
class PlansModel(models.Model):
    pname=models.CharField(max_length=50)
    pvalidity=models.IntegerField()
    pdata=models.IntegerField()
    ptalktime=models.IntegerField()
    service=models.CharField(max_length=50)
    device=models.CharField(max_length=50)


class PrepaidMobileCustomerModel(models.Model):
    cid=models.IntegerField()
    planid=models.IntegerField()
    planname=models.CharField(max_length=50,default=None)
    activatestatus=models.BooleanField()
    pactivateddate=models.DateTimeField()
    pexpirydate=models.DateTimeField(default=None)
    pcurrentdate=models.DateTimeField(default=None)
    paymentype=models.CharField(max_length=50,default=None)
    pdata=models.IntegerField(default=None)
    psms=models.IntegerField(default=None)
    pvalidity=models.IntegerField(default=None)
    pvoice=models.IntegerField(default=None)


class PrepaidMobilePlansModel(models.Model):
    pname=models.CharField(max_length=50)
    pvalidity=models.IntegerField()
    pdata=models.IntegerField()
    ptalktime=models.IntegerField()
    psms=models.IntegerField()
    ptype=models.CharField(max_length=50)

class BillManagementModel(models.Model):
    billnumber=models.IntegerField()
    cid=models.IntegerField()
    planid=models.IntegerField()
    transactiontype=models.CharField(max_length=50)
    pactivateddate=models.DateTimeField(default=datetime.now)
    amount=models.IntegerField()
    servicetype=models.CharField(max_length=50)
class PlanPostpaidMobile(models.Model):
    plan_name = models.IntegerField()
    data = models.IntegerField()
    SMS = models.IntegerField()
    calls = models.CharField(max_length=50)
    subs = models.CharField(max_length=50)

class Usagemodel(models.Model):
    planid=models.IntegerField()
    cid=models.IntegerField()
    cdata=models.IntegerField(default=None)
    csms=models.IntegerField(default=None)
    cvalidity=models.IntegerField(default=None)
    cvoice=models.IntegerField(default=None)

class Filldetailpostpaid(models.Model):
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

class Usagepostpaid(models.Model):
    plan_name = models.IntegerField()
    plan_status = models.CharField(max_length=50)
    used_data = models.IntegerField()
    used_sms = models.IntegerField()
    used_call = models.CharField(max_length=50)

class Accountsummarypost(models.Model):
    previous_bal = models.IntegerField()
    Adjustment = models.CharField(max_length=50)
    month_charge = models.CharField(max_length=50)
    amount_due = models.CharField(max_length=50)

class Servicepostpaid(models.Model):
    bill_no = models.IntegerField()
    bill_data = models.CharField(max_length=50)
    bill_period = models.CharField(max_length=50)
    pay_date = models.CharField(max_length=50)

class Monthchargepost(models.Model):
    monthly_rent = models.IntegerField()
    usage = models.CharField(max_length=50)
    one_time_charge = models.IntegerField()
    discounts = models.IntegerField()
    taxes = models.IntegerField()

class PostpaidDongleCustomerModel(models.Model):
    cid=models.IntegerField()
    planid=models.IntegerField()
    activatestatus=models.BooleanField()
    pactivateddate=models.DateTimeField()
    pexpirydate=models.DateTimeField(default=None)

class PostpaidDonglePlansModel(models.Model):
    pname=models.CharField(max_length=100)
    pvalidity=models.CharField(max_length=50)
    pdata=models.CharField(max_length=50)
    ptype=models.CharField(max_length=1000)
    sms=models.CharField(max_length=1000)
    subscription=models.CharField(max_length=1000)
    
class PrepaidDonglePlansModel(models.Model):
    pname=models.CharField(max_length=100)
    pvalidity=models.CharField(max_length=50)
    pdata=models.CharField(max_length=50)
    ptalktime=models.CharField(max_length=50)
    ptype=models.CharField(max_length=50)

class PrepaidDongleCustomerModel(models.Model):
    cid=models.IntegerField()
    planid=models.IntegerField()
    activatestatus=models.BooleanField()
    pactivateddate=models.DateTimeField()
    pexpirydate=models.DateTimeField(default=None)
    paymentype=models.CharField(max_length=50,default=None)
class AddloginModel(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class AdminRegisterModel(models.Model):
    ename=models.CharField(max_length=200)
    eemail=models.CharField(max_length=200)
    epassword=models.CharField(max_length=200)
    emobile=models.BigIntegerField()

class AdminloginModel(models.Model):
    eusername=models.CharField(max_length=200)
    epassword=models.CharField(max_length=200)
   

class Dongleregister(models.Model):
    dname = models.CharField(max_length=50)
    daddress = models.CharField(max_length=50)
    daddress_1 = models.CharField(max_length=50)
    dcity = models.CharField(max_length=50)
    dstate = models.CharField(max_length=50)
    dpincode = models.CharField(max_length=50)
    demail = models.CharField(max_length=50)
    dphn = models.CharField(max_length=50)
    
class contactModel(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)

