
from django.db import models
from rest_framework import fields, serializers
from voiceapp.models import PlansModel, PostpaidDongleCustomerModel, PostpaidDonglePlansModel, PrepaidDonglePlansModel,Usagemodel,contactModel
from voiceapp.models import PrepaidDongleCustomerModel,RegisterModel,PrepaidMobilePlansModel,PrepaidMobileCustomerModel,BillManagementModel
from voiceapp.models import PlanPostpaidMobile,Filldetailpostpaid,AdminloginModel,AdminRegisterModel,Usagepostpaid,Accountsummarypost,Servicepostpaid,Monthchargepost,AddloginModel
from voiceapp.models import PlanPostpaidMobile,Filldetailpostpaid,Usagepostpaid,Accountsummarypost,Servicepostpaid,Monthchargepost,AddloginModel
from voiceapp.models import Dongleregister

from voiceapp.models import PlanPostpaidMobile,Filldetailpostpaid,AdminloginModel,AdminRegisterModel,Usagepostpaid,Accountsummarypost,Servicepostpaid,Monthchargepost,AddloginModel

from voiceapp.models import PlanPostpaidMobile,Filldetailpostpaid,Usagepostpaid,Accountsummarypost,Servicepostpaid,Monthchargepost,AddloginModel
from voiceapp.models import Dongleregister

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlansModel
        fields=('id','pname','pvalidity','pdata','ptalktime','service','device')
class PrepaidMobilePlansSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrepaidMobilePlansModel
        fields=('id','pname','pvalidity','pdata','ptalktime','psms','ptype')


class RegisterSerializer(serializers.ModelSerializer):
    aadharphoto=serializers.ImageField()
    profilephoto=serializers.ImageField()
    class Meta:
        model=RegisterModel
        fields=('id','cname','profilephoto','email','password','mobile','aadhar','aadharphoto','device','service')

class PlanSerializerpost(serializers.ModelSerializer):
    class Meta:
        model=PlanPostpaidMobile
        fields = ("id","plan_name","data","SMS","calls","subs")

class DetailpostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Filldetailpostpaid
        fields = ("id","name","mobile_no","address","address_1","state","city","pincode")

class usagepostpaidSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usagepostpaid
        fields = ("id","plan_name","plan_status","used_data","used_sms","used_call")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accountsummarypost
        fields = ("id","previous_bal","Adjustment","month_charge","amount_due")

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicepostpaid
        fields = ("id","bill_no","bill_data","bill_period","pay_date")

class MonthchargeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Monthchargepost
        fields = ("id","monthly_rent","usage","one_time_charge","discounts","taxes")

class PreDonglecustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrepaidDongleCustomerModel
        fields=('cid','planid','activatestatus','pactivateddate','pexpirydate')

class PrepaidMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrepaidMobileCustomerModel
        fields=('cid','planname','planid','activatestatus','pactivateddate','pexpirydate','paymentype','pvoice','pdata','psms','pvalidity','pcurrentdate')

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillManagementModel
        fields=('billnumber','cid','planid','transactiontype','pactivateddate','amount','servicetype')

class PreDonglecustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrepaidDongleCustomerModel
        fields=('cid','planid','activatestatus','pactivateddate','pexpirydate')

class PostDonglecustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostpaidDongleCustomerModel
        fields=('cid','planid','activatestatus','pactivateddate','pexpirydate')

class PrepaidDonglePlansSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrepaidDonglePlansModel
        fields=('id','pname','pvalidity','pdata','ptalktime','ptype')

class PostpaidDonglePlansSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostpaidDonglePlansModel
        fields=('id','pname','pvalidity','pdata','ptype','sms','subscription')
class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usagemodel
        fields=('id','planid','cid','csms','cdata','cvalidity','cvoice')

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddloginModel
        fields=('id','username','password')


class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminRegisterModel
        fields=('id','ename','eemail','epassword','emobile')

class AdminloginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminloginModel
        fields=('id','eusername','epassword')

class DongleregiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongleregister
        fields = ("id","dname","daddress","daddress_1","dcity","dstate","dpincode","demail","dphn")
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model=contactModel
        fields=('id','firstname','lastname','country','subject')

