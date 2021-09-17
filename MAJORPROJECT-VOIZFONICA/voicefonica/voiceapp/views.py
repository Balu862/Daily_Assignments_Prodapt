from django.conf import settings
import pdfkit
from django.shortcuts import redirect, render
from django.core.mail import send_mail,EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils.serializer_helpers import ReturnDict
from voiceapp.models import PlansModel, PostpaidDongleCustomerModel, PostpaidDonglePlansModel, PrepaidDongleCustomerModel, PrepaidDonglePlansModel,RegisterModel,PrepaidMobilePlansModel,PrepaidMobileCustomerModel,Usagemodel,contactModel,BillManagementModel
from voiceapp.serializer import PlanSerializer, PostDonglecustomerSerializer, PostpaidDonglePlansSerializer, PrepaidDonglePlansSerializer, PrepaidMobilePlansSerializer,RegisterSerializer,PrepaidMobilePlansModel,PrepaidMobileSerializer,contactSerializer,BillSerializer
from voiceapp.serializer import PreDonglecustomerSerializer,UsageSerializer
from voiceapp.models import PlansModel, PostpaidDongleCustomerModel,AdminRegisterModel, AdminloginModel, PostpaidDonglePlansModel, PrepaidDongleCustomerModel, PrepaidDonglePlansModel,RegisterModel,PrepaidMobilePlansModel,PrepaidMobileCustomerModel
from voiceapp.serializer import PlanSerializer,AdminRegisterSerializer, AdminloginSerializer, PostDonglecustomerSerializer, PostpaidDonglePlansSerializer, PrepaidDonglePlansSerializer, PrepaidMobilePlansSerializer,RegisterSerializer,PrepaidMobilePlansModel,PrepaidMobileSerializer
from voiceapp.serializer import PreDonglecustomerSerializer,loginSerializer
from voiceapp.serializer import PlanSerializerpost,DetailpostSerializer,usagepostpaidSerializer,AccountSerializer,ServiceSerializer,MonthchargeSerializer
from voiceapp.models import PlanPostpaidMobile,Filldetailpostpaid,Usagepostpaid,Accountsummarypost,Servicepostpaid,Monthchargepost
from django.http import HttpResponse,JsonResponse
from rest_framework import status
import requests,json
from rest_framework.parsers import JSONParser
from datetime import datetime,timedelta
import random
from django.contrib import messages

# from fpdf import FPDF
# import pdfkit
# from fpdf import FPDF
#dongle register#
from voiceapp.serializer import DongleregiSerializer
from voiceapp.models import Dongleregister


def head(request):
    return render(request,'dashboardheader.html')



def home(request):
    a="home"
    if request.session.has_key('user'):
        del request.session['user']
        print("deleted")
    else:
        print("noot deleted")
    return render(request,'homeheader.html',{'home':a})

@csrf_exempt
def addplan(request):
    if (request.method=="POST"):
        # dict1=JSONParser().parse(request)
        # result=json.dumps(dict1)
        # print(result)
        planadd=PrepaidMobilePlansSerializer(data=request.POST)
        if (planadd.is_valid()):
            print(1)
            planadd.save()
            return JsonResponse(planadd.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_404_NOT_FOUND) 
    else:
        return HttpResponse("Get method not allowed")
def mprepaidadd(request):
    return render(request,"admin/mprepaidaddplan.html")
        
@csrf_exempt
def Registration(request):
    if request.method=="POST":
        username=request.POST.get('aadhar')
        data=RegisterModel.objects.filter(aadhar=username)
        if data:
            messages="user id exist please login"
            return redirect(Login)
        else:
            print(1)
            cname=request.POST.get('cname')
            profilephoto=request.FILES['profilephoto']
            email=request.POST.get('email')
            password=request.POST.get('password')
            mobile=request.POST.get('mobile')
            aadhar=request.POST.get('aadhar')
            aadharfile=request.FILES['aadharphoto']
            device=request.POST.get('device')
            service=request.POST.get('service')
            dict1={'cname':cname,'profilephoto':profilephoto,'email':email,'password':password,'mobile':mobile,'aadhar':aadhar,'aadharphoto':aadharfile,'device':device,'service':service}
            print(dict1)
            registereddata=RegisterSerializer(data=dict1)
            print(registereddata)
            if registereddata.is_valid():
                registereddata.save()
                
                return redirect(Login)
            else:
                    print(registereddata.errors)
            
    return render(request,'registration.html')
@csrf_exempt
def Login(request):
    if request.method=="POST":
        print(1)
        username=request.POST.get('username')
        password1=request.POST.get('password')
        flag=0
        data=RegisterModel.objects.filter(email=username,password=password1)
        print(data)
        if data:
            userserialiser=RegisterSerializer(data,many=True)
            request.session['user']=userserialiser.data
            print(request.session['user'])
            a="login"
            return redirect(Index)
    return render(request,'login.html')

@csrf_exempt
def truelyunlimeted(request):
    data=PrepaidMobilePlansModel.objects.filter(ptype="trulyunlimited")
    return render(request,"mobileprepaid/truleyunlimted.html",{"data":data})
@csrf_exempt
def intlr(request):
    data=PrepaidMobilePlansModel.objects.filter(ptype="intlr")
    return render(request,"mobileprepaid/intlr.html",{'data':data})
@csrf_exempt
def smartrecharge(request):
    data=PrepaidMobilePlansModel.objects.filter(ptype="smartrecharge")
    return render(request,"mobileprepaid/smartrecharge.html",{'data':data})
@csrf_exempt
def data(request):
    data=PrepaidMobilePlansModel.objects.filter(ptype="data")
    return render(request,'mobileprepaid/data.html',{'data':data})
@csrf_exempt
def talktime(request):
    data=PrepaidMobilePlansModel.objects.filter(ptype="talktime")
    return render(request,"mobileprepaid/talktime.html",{'data':data})
@csrf_exempt
def homeprepaid(request):
    a="prepaid"
    return render(request,'homeheader.html',{"prepaid":a})

@csrf_exempt
def Index(request):
    a="index"
    if request.session.has_key('user'):
        return render(request,'index.html',{"index":a})
    else:
        return redirect(home)
def Prepaid(request):
    if request.session.has_key('user'):
        a="prepaid"
        userdetails=request.session['user']
        userdetails=userdetails[0]
        data=PrepaidMobileCustomerModel.objects.filter(cid=userdetails['id'])
        if data:
            data=PrepaidMobileSerializer(data,many=True)
           # print(data)
            data=data.data
           # print(data)
            plandetails=[]
            
            usagedata=Usagemodel.objects.filter(cid=userdetails['id'])
            if usagedata:
                usagedetails=UsageSerializer(usagedata,many=True)
                print("useagedetails",usagedetails.data)
                usagedetails=usagedetails.data
                for i in usagedetails:
                    print(i['planid'])
                    change=PrepaidMobileCustomerModel.objects.get(planid=i['planid'],cid=userdetails['id'])
                    changeserializer=PrepaidMobileSerializer(change)
                    changeserializer=changeserializer.data
                    print(changeserializer)
                    chdata=changeserializer['pdata']-i['cdata']
                    if chdata<0:
                        chdata=0
                    chsms=changeserializer['psms']-i['csms']
                    if chsms<0:
                        chsms=0
                    chval=changeserializer['pvalidity']-i['cvalidity']
                    if chval<0:
                        chval=0
                        change.delete()
                        usagedata.delete()
                        return redirect(Index)
                    chvoice=changeserializer['pvoice']-i['cvoice']
                    if chvoice<0:
                        chvoice=0
                    changed=PrepaidMobileCustomerModel.objects.filter(planid=i['planid'],cid=userdetails['id']).update(pdata=chdata,psms=chval,pvalidity=chval,pvoice=chvoice)
                    print("changeddata",changed)
    
            plandetails=PrepaidMobileCustomerModel.objects.all()
            #print(plandetails)
            print(plandetails)
            usagedata.delete()
            return render(request,'index.html',{"prepaid":plandetails})
        else:
            return render(request,'index.html',{"noprepaid":a})
    else:
        return redirect(home)

def pdata(request):
    if request.session.has_key('user'):
        a=1
        return render(request,"index.html",{'prepaiddetails':a})
    else:
        return redirect(home)
@csrf_exempt
def dintlr(request):
    if request.session.has_key('user'):
        data=PrepaidMobilePlansModel.objects.filter(ptype="intlr")
        return render(request,"mobileprepaid/dintlr.html",{'data':data})
    else:
        return redirect(home)
@csrf_exempt
def dsmartrecharge(request):
    if request.session.has_key('user'):
        data=PrepaidMobilePlansModel.objects.filter(ptype="smartrecharge")
        return render(request,"mobileprepaid/dsmartrecharge.html",{'data':data})

    else:
        return redirect(home)

@csrf_exempt
def ddata(request):
    if request.session.has_key('user'):
        data=PrepaidMobilePlansModel.objects.filter(ptype="data")
        return render(request,'mobileprepaid/ddata.html',{'data':data})
    else:
        return redirect(home)
@csrf_exempt
def dtalktime(request):
    if request.session.has_key('user'):
        data=PrepaidMobilePlansModel.objects.filter(ptype="talktime")
        return render(request,"mobileprepaid/dtalktime.html",{"data":data})
    else:
        return redirect(home)
@csrf_exempt
def dtruelyunlimeted(request):
    if request.session.has_key('user'):
        data=PrepaidMobilePlansModel.objects.filter(ptype="trulyunlimited")
        return render(request,"mobileprepaid/dtruelyunlimited.html",{"data":data})
    else:
        return redirect(home)

@csrf_exempt
def paymentpre(request):
    planid=request.POST.get('id')
    return render(request,'payment.html',{"planid":planid})

@csrf_exempt
def prepaidcustomer(request):
    if request.session.has_key('user'):
        if request.method=="POST":
            userdetails=request.session['user']
            userdetails=userdetails[0]
            planid=request.POST.get('id')
            paymenttype=request.POST.get('paymentype')
            print(planid,paymenttype)
            plandata=PrepaidMobilePlansModel.objects.get(id=planid)
            userid=userdetails['id']
            activate=True
            current_date = datetime.now()
            plandata=PrepaidMobilePlansSerializer(plandata)
            plandata=plandata.data
            print(plandata)
            expirydate=datetime.now()+timedelta(days=plandata['pvalidity'])
            pdata1=plandata['pdata']
            psms=plandata['psms']
            pvalidity=plandata['pvalidity']
            pvoice=plandata['ptalktime']
            planname=plandata['pname']
            dict1={'planname':planname,'planid':planid,'cid':userid,'activatestatus':activate,'pactivateddate':str(current_date),'pexpirydate':expirydate,'paymentype':paymenttype,'pvoice':pvoice,'pdata':pdata1,'psms':psms,'pvalidity':pvalidity,'pcurrentdate':current_date}
            addserializer=PrepaidMobileSerializer(data=dict1)
            if addserializer.is_valid():
                addserializer.save()
                plandata=PrepaidMobilePlansSerializer(plandata)
                request.session['currentplan']=plandata.data
                return redirect(billgeneration)

            else:
                return JsonResponse(addserializer.errors)
        else:
            return JsonResponse("Only post is allowed")

@csrf_exempt
def billgeneration(request):
    billnumber=random.randrange(10000,99999)
    obj1=PrepaidMobileCustomerModel.objects.all()
    obj1=obj1[len(obj1)-1]
    data=PrepaidMobileSerializer(obj1)
    print("data",data.data)
    data=data.data
    userdata=RegisterModel.objects.get(id=data['cid'])
    plandata=PrepaidMobilePlansModel.objects.get(id=data['planid'])

    return render(request,'mobileprepaid/bill.html',{'data':obj1,'userdata':userdata,'plandata':plandata,'billnumber':billnumber})
@csrf_exempt
def BillManagement(request):
    if request.session.has_key('user'):
        if request.method=="POST":
            billnumber=random.randrange(10000,99999)
            customerinfo=request.session['user']
            customerinfo=customerinfo[0]
            time=str(datetime.now())
            print("time",time)
            pdfname="bill/"+str(customerinfo['cname'])+str(datetime.now())+".pdf"
            time=time.split(".")
            time=time[0]
            n=str(customerinfo['cname'])+str(time)
            new_string = ''.join(filter(str.isalnum,n)) 
            print(new_string)
            pdfname="bill/"+new_string+".pdf"
            print("pdfname",pdfname)
            try:
                pdfkit.from_url("http://127.0.0.1:8000/voice/billgeneration",pdfname)  
            except:
                print("yes bill is saved")
            subject="Voizfonicabill"
            to=customerinfo['email']
            print("to",to)
            body="Your bill is Generated"
            msg=EmailMessage(subject,body,settings.EMAIL_HOST_USER,[to])
            msg.attach_file(pdfname)
            msg.send()
            print("mail is sent")
            pdfname=pdfname+" (application/pdf)"
            planid=request.POST.get('planid')
            print("planid",planid)
            transaction=request.POST.get('transactiontype')
            planname=request.POST.get('planname')
            dict1={'billnumber':billnumber,'cid':customerinfo['id'],'planid':int(planid),'transactiontype':transaction,'pactivateddate':datetime.now(),'amount':int(planname),'servicetype':"prepaid"}
            billdata=BillSerializer(data=dict1)
            print(billdata)
            if billdata.is_valid():
                billdata.save()
                print(billdata.data)
                print("yes bill is saved to database")
            else:
                print(billdata.errors)
 
            return redirect(Index)
        else:
            return HttpResponse("only post is allowed")
#postpaid#
@csrf_exempt
def BillManagementpost(request):
    if request.session.has_key('user'):
        if request.method=="POST":
            billnumber=random.randrange(10000,99999)
            customerinfo=request.session['user']
            customerinfo=customerinfo[0]
            time=str(datetime.now())
            print("time",time)
            pdfname="bill/"+str(customerinfo['cname'])+str(datetime.now())+".pdf"
            time=time.split(".")
            time=time[0]
            n=str(customerinfo['cname'])+str(time)
            new_string = ''.join(filter(str.isalnum,n)) 
            print(new_string)
            pdfname="bill/"+new_string+".pdf"
            print("pdfname",pdfname)
            new_string=new_string+".pdf"
            try:
                pdfkit.from_url("http://127.0.0.1:8000/voice/bill/",pdfname)  
            except:
                print("yes bill is saved")
            subject="Voizfonicabill"
            to=customerinfo['email']
            print("to",to)
            body="Your bill is Generated"
            msg=EmailMessage(subject,body,settings.EMAIL_HOST_USER,[to])
            msg.attach_file(pdfname)
            msg.send()
            print("mail is sent")
            return redirect(Index)
        else:
            return HttpResponse("only post is allowed")
@csrf_exempt
def usage(request):
    usagedata=PrepaidMobileCustomerModel.objects.all()
    if request.method=="POST":
        usagedata=UsageSerializer(data=request.POST)
        if usagedata.is_valid():
            usagedata.save()
            print("usagesaved")
            return redirect(Index)
        else:
            print(usagedata.errors)
            return HttpResponse(usagedata.errors)
    return render(request,'mobileprepaid/usage.html',{"data":usagedata})
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    if request.session.has_key('currentplan'):
        del request.session['currentplan']
    return redirect(home)

#postpaid mobile#
def postpage(request):
    fetchdatas = requests.get("http://127.0.0.1:8000/voice/usageview/").json()
    return render(request,'mobilepostpaid/post.html',{"datas":fetchdatas})

def view_mobile_post_plan(request):
    fetchdata = requests.get("http://127.0.0.1:8000/voice/postview/").json()
    return render(request,'mobilepostpaid/viewspostmobile.html',{"data":fetchdata})

def dview_mobile_post_plan(request):
    fetchdata = requests.get("http://127.0.0.1:8000/voice/postview/").json()
    return render(request,'mobilepostpaid/dviewspostmobile.html',{"data":fetchdata})

def detail_fill_post(request):
    return render(request,'mobilepostpaid/detailfillpostpaid.html')

def billpaid(request):
    #fetch = requests.get("http://127.0.0.1:8000/voice/detailshow/").json()

    fetchaccount = requests.get("http://127.0.0.1:8000/voice/accountview/").json()
    fetchservice = requests.get("http://127.0.0.1:8000/voice/serviceview/").json()
    fetchmonth = requests.get("http://127.0.0.1:8000/voice/monthlyview/").json()
    return render(request,'mobilepostpaid/billshowpostpaid.html',{"data_acc":fetchaccount,"data_ser":fetchservice,"data_mon":fetchmonth})

def pay(request):
    return render(request,'mobilepostpaid/paypostpaid.html')

def payment(request):
    return render(request,'mobilepostpaid/paymentmobilepost.html')

def submitpostpaid(request):
    return render(request,'mobilepostpaid/submitpost.html')

def successpost(request):
    return render(request,'mobilepostpaid/success.html')

def viewpostcustomer(request):
    fetch = requests.get("http://127.0.0.1:8000/voice/detailshow/").json()
    return render(request,'admin/postpaidcutomerview.html',{"data":fetch})

@csrf_exempt
def planpostpaid(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        pay_serializer = PlanSerializerpost(data=request.POST)
        if(pay_serializer.is_valid()):
            pay_serializer.save()
            return JsonResponse(pay_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

def mpostadd(request):
    return render(request,"admin/mpostpaidaddplan.html")

@csrf_exempt
def viewplanpost(request):
    if(request.method == "GET"):
        planpost = PlanPostpaidMobile.objects.all()
        pay_serializer = PlanSerializerpost(planpost,many=True)
        return JsonResponse(pay_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def view_oneplan(request,id):
    try:
        planpost=PlanPostpaidMobile.objects.get(id=id)
    except PlanPostpaidMobile.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        plan_serializer = PlanSerializerpost(planpost)
        return JsonResponse(plan_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        plan_serializer = PlanSerializerpost(planpost,data=mydata)
        if(plan_serializer.is_valid()):
            plan_serializer.save()
            return JsonResponse(plan_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serilaizer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        planpost.delete()
        return JsonResponse("Deleted item",status=status.HTTP_200_OK)

@csrf_exempt
def filldetailpost(request):
    if(request.method == "POST"):
        # data = JSONParser().parse(request)
        # detail_serializer = DetailpostSerializer(data=data)
        detail_serializer = DetailpostSerializer(data=request.POST)
        if(detail_serializer.is_valid()):
            detail_serializer.save()
            messages.success(request, 'Postpaid Registerd')
            return redirect(billpaid)
            # return JsonResponse(detail_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def detail_post_show(request):
    if(request.method == "GET"):
        # id=request.session['user']
        # id=id[0]
        # id=id['cname']
    
        detail = Filldetailpostpaid.objects.all()
        detail_serializer = DetailpostSerializer(detail,many=True)
        return JsonResponse(detail_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def usage_add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        usage_serializer = usagepostpaidSerializer(data=mydata)
        if(usage_serializer.is_valid()):
            usage_serializer.save()
            return JsonResponse(usage_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def usage_view(request):
    if(request.method == "GET"):
        usage = Usagepostpaid.objects.all()
        usage_serializer = usagepostpaidSerializer(usage,many=True)
        return JsonResponse(usage_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def account_add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=mydata)
        if(account_serializer.is_valid()):
            account_serializer.save()
            return JsonResponse(account_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def account_view(request):
    if(request.method == "GET"):
        account = Accountsummarypost.objects.all()
        account_serializer = AccountSerializer(account,many=True)
        return JsonResponse(account_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def service_add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        service_serializer = ServiceSerializer(data=mydata)
        if(service_serializer.is_valid()):
            service_serializer.save()
            return JsonResponse(service_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def service_view(request):
    if(request.method == "GET"):
        service = Servicepostpaid.objects.all()
        service_serializer = ServiceSerializer(service,many=True)
        return JsonResponse(service_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def monthly_add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        monthly_serializer = MonthchargeSerializer(data=mydata)
        if(monthly_serializer.is_valid()):
            monthly_serializer.save()
            return JsonResponse(monthly_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def monthly_view(request):
    if(request.method == "GET"):
        monthly = Monthchargepost.objects.all()
        monthly_serializer = MonthchargeSerializer(monthly,many=True)
        return JsonResponse(monthly_serializer.data,safe=False,status=status.HTTP_200_OK)

####################### PREPAID DONGLE ###############################################

@csrf_exempt
def homeprepaiddongle(request):
    a="prepaiddongle"
    return render(request,'homeheader.html',{"prepaiddongle":a})

@csrf_exempt
def predongletruleyunlimted(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Truly Unlimited")
    print(data)
    return render(request,"dongleprepaid/predongletruly.html",{'data':data})

@csrf_exempt
def predonglesmartrecharge(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Smart Recharge")
    print(data)
    return render(request,"dongleprepaid/predonglesmart.html",{'data':data})

@csrf_exempt
def predongledata(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Data")
    print(data)
    return render(request,"dongleprepaid/predongledata.html",{'data':data})


def prepaiddongle(request):
    return render(request,'dongleprepaid/prepaiddongle.html')

def trulydongleunlimeted(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Truly Unlimited")
    print(data)
    return render(request,"dongleprepaid/truelydongleunlimited.html",{"data":data})

def donglesmartrecharge(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Smart Recharge")
    return render(request,"dongleprepaid/smartrecharge.html",{"data":data})


def dongledata(request):
    data=PrepaidDonglePlansModel.objects.filter(ptype="Data")
    return render(request,"dongleprepaid/dongledata.html",{"data":data})



@csrf_exempt
def addpredongleplan(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        plan_serializer = PrepaidDonglePlansSerializer(data=request.POST)
        if(plan_serializer.is_valid()):
            plan_serializer.save()
            print("YES")
            return HttpResponse("OK")
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)

def dprepaidadd(request):
    return render(request,"admin/dongprepaidaddplan.html")


def PrepaidDonglecustomer(request):
    if request.session.has_key('user'):

        a="prepaiddongle"
        userdetails=request.session['user']
        userdetails=userdetails[0]
        data=PrepaidDongleCustomerModel.objects.filter(cid=userdetails['id'])
        print("123")
        if data:
            data=PreDonglecustomerSerializer(data,many=True)
            print(data)
            data=data.data
            print(data)
            plandetails=[]
            for i in data:

            
                planid=i['planid']
                plandata=PrepaidDonglePlansModel.objects.get(id=planid)
                plandetails.append(plandata)
            print(plandetails)
            return render(request,'index.html',{"prepaiddongle":plandetails})
        else:
            print("NO PREPAID")
            return render(request,'index.html',{"noprepaiddongle":a})
    else:
        return redirect(home)


@csrf_exempt
def prepaidDonglePlan(request):
    if request.session.has_key('user'):
        if request.method=="POST":
            userdetails=request.session['user']
            userdetails=userdetails[0]
            planid=request.POST.get('id')
            print(planid)
            paymenttype=request.POST.get('paymentype')
            print(planid,paymenttype)
            plandata= PrepaidDonglePlansModel.objects.get(id=planid)
            userid=userdetails['id']
            activate=True
            current_date = datetime.now()
            plandata=PrepaidDonglePlansSerializer(plandata)
            plandata=plandata.data
            print(plandata)
            expirydate=datetime.now()+timedelta(0.02)    
            dict1={'planid':planid,'cid':userid,'activatestatus':activate,'pactivateddate':str(current_date),'pexpirydate':expirydate,'paymentype':paymenttype}
            addserializer=PreDonglecustomerSerializer(data=dict1)
            if addserializer.is_valid():
                addserializer.save()
                plandata=PrepaidDonglePlansSerializer(plandata)
                request.session['currentplan']=plandata.data
                return render(request,'mobileprepaid/bill.html',{'data':dict1})

            else:
                return JsonResponse(addserializer.errors)

        else:
            return HttpResponse("Only Post is allowed")
    
    else:
        return HttpResponse("No user found")
            

def predongledata(request):
    a=1
    return render(request,"index.html",{'prepaiddongledetails':a})

@csrf_exempt
def paymentpredong(request):
    planid=request.POST.get('id')
    return render(request,'paymentpredong.html',{"planid":planid})


###################### POSTPAID DONGLE #################################

@csrf_exempt
def homepostpaiddongle(request):
    a="prepaid"
    return render(request,'homeheader.html',{"postpaiddongle":a})


def Postpaiddongle(request):
    return render(request,'postpaiddongle.html')

@csrf_exempt
def addpostdongleplan(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        plan_serializer = PostpaidDonglePlansSerializer(data=request.POST)
        if(plan_serializer.is_valid()):
            plan_serializer.save()
            print("YES")
            return HttpResponse("OK")
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)

def dpostpaidadd(request):
    return render(request,'admin/dongpostpaidaddplan.html')



def PostpaidDonglecustomer(request):
    if request.session.has_key('user'):
        a="postpaiddongle"
        userdetails=request.session['user']
        userdetails=userdetails[0]
        data=PostpaidDongleCustomerModel.objects.filter(cid=userdetails['id'])
        if data:
            data=PostDonglecustomerSerializer(data,many=True)
            print(data)
            data=data.data
            print(data)
            plandetails=[]
            for i in data:
                
                planid=i['planid']
                plandata=PostpaidDonglePlansModel.objects.get(id=planid)
                plandetails.append(plandata)
            print(plandetails)
            return render(request,'index.html',{"postpaiddongle":plandetails})
        else:
            print("NO PREPAID")
            return render(request,'index.html',{"nopostpaiddongle":a})
    else:
        return redirect(home)


               

@csrf_exempt
def postdongleplans(request):
    data=PostpaidDonglePlansModel.objects.filter(ptype="Truly Unlimited")
    print(data)
    return render(request,"donglepostpaid/postpaiddongleplans.html",{'data':data})


@csrf_exempt
def postpaidDonglePlan(request):
    if request.session.has_key('user'):
        if request.method=="POST":           
            userdetails=request.session['user']
            userdetails=userdetails[0]
            planid=request.POST.get('id')
            print(planid)
            plandata= PostpaidDonglePlansModel.objects.get(id=planid)
            userid=userdetails['id']
            activate=True
            current_date = datetime.now()
            plandata=PostpaidDonglePlansSerializer(plandata)
            plandata=plandata.data
            print(plandata)
            expirydate=datetime.now()+timedelta(0.02)    
            dict1={'planid':planid,'cid':userid,'activatestatus':activate,'pactivateddate':str(current_date),'pexpirydate':expirydate}
            addserializer=PostDonglecustomerSerializer(data=dict1)
            if addserializer.is_valid():
                addserializer.save()
                plandata=PostpaidDonglePlansSerializer(plandata)
                request.session['currentplan']=plandata.data
                return render(request,'mobileprepaid/bill.html',{'data':dict1})

            else:
                return JsonResponse(addserializer.errors)

        else:
            return JsonResponse("Only post is allowed")


def postdongledata(request):
    a=1
    print(a)
    return render(request,"dashboardheader.html",{'postpaiddongledetails':a})

def postpaidDdata(request):
    data=PostpaidDonglePlansModel.objects.filter(ptype="Unlimited")
    return render(request,"donglepostpaid/postpaiddongle.html",{"data":data})
    




'''
{% if request.session.user %}
  {% include 'dashboardheader.html' %}
 
{% else %}
  {% include 'homeheader.html' %}
{% endif %}
{% include 'mobileprepaid/header.html' %}
{% block mycontent %}'''



'''
{% extends 'homeheader.html' %}
{% block home %}
{% include 'mobileprepaid/header.html' %}
{% block mycontent %}'''

#HELP DESK#

def faqhome(request):
    return render(request,'FAQ/FAQhome.html')

def faqposthome(request):
    return render(request,'FAQ/FAQPOSThome.html')

def faqpostplan(request):
    return render(request,'FAQ/FAQPOSTplan.html')

def faqpostbill(request):
    return render(request,'FAQ/FAQPOSTbill.html')

def faqpostdata(request):
    return render(request,'FAQ/FAQPOSTdata.html')

def faqpostproduct(request):
    return render(request,'FAQ/FAQPOSTproduct.html')

def faqpostactivate(request):
    return render(request,'FAQ/FAQPOSTactivate.html')

def faqpostother(request):
    return render(request,'FAQ/FAQPOSTother.html')

def faqprehome(request):
    return render(request,'FAQ/FAQPREhome.html')

def faqpregeneral(request):
    return render(request,'FAQ/FAQPREgeneral.html')

def faqpreproduct(request):
    return render(request,'FAQ/FAQPREproduct.html')

def faqpredata(request):
    return render(request,'FAQ/FAQPREdata.html')

def faqdonghome(request):
    return render(request,'FAQ/FAQDONGhome.html')

def faqdonggeneral(request):
    return render(request,'FAQ/FAQDONGgeneral.html')
    
#help desk webpage#
def faqhomepage(request):
    return render(request,'FAQwebpage/FAQhomepage.html')

def faqposthomepage(request):
    return render(request,'FAQwebpage/FAQposthome.html')

def faqpostplanpage(request):
    return render(request,'FAQwebpage/FAQpostplan.html')

def faqpostbillpage(request):
    return render(request,'FAQwebpage/FAQpostbill.html')

def faqpostdatapage(request):
    return render(request,'FAQwebpage/FAQpostdata.html')

def faqpostproductpage(request):
    return render(request,'FAQwebpage/FAQpostproduct.html')

def faqpostactivatepage(request):
    return render(request,'FAQwebpage/FAQpostactivate.html')

def faqpostotherpage(request):
    return render(request,'FAQwebpage/FAQpostother.html')

def faqprehomepage(request):
    return render(request,'FAQwebpage/FAQprehome.html')

def faqpregeneralpage(request):
    return render(request,'FAQwebpage/FAQpregeneral.html')

def faqpreproductpage(request):
    return render(request,'FAQwebpage/FAQpreproduct.html')

def faqpredatapage(request):
    return render(request,'FAQwebpage/FAQpredata.html')

def faqdonghomepage(request):
    return render(request,'FAQwebpage/FAQdonghome.html')

def faqdonggeneralpage(request):
    return render(request,'FAQwebpage/FAQdongeneral.html')



################################## Admin  #############################################

def adminhomepage(request):
    return render(request,'admin/adminhome.html')

def adminloginpage(request):
    return render(request,'admin/adminlogin.html')

def adminregistrationpage(request):
    return render(request,'admin/adminregistrationr.html')

def adminnhome(request):
    a="adminhomepage"
    if request.session.has_key('user'):
        del request.session['user']
        print("deleted")
    else:
        print("noot deleted")
    return render(request,'admin/adminhome.html',{'adminhomepage':a})

@csrf_exempt
def adminRegistration(request):
    if request.method=="POST":
        username=request.POST.get('eemail')
        data=AdminRegisterModel.objects.filter(eemail=username)
        if data:
            messages="user id exist please login"
            return redirect(adminLogin)
        else:
            print(1)
            getname=request.POST.get('ename')       
            getemail=request.POST.get('eemail')
            getpassword=request.POST.get('epassword')
            getmobile=request.POST.get('emobile')
            dict1={'ename':getname,'eemail':getemail,'epassword':getpassword,'emobile':getmobile}
            print(dict1)
            registereddata=AdminRegisterSerializer(data=dict1)
            print(registereddata)
            if registereddata.is_valid():
                registereddata.save()
                return redirect(adminLogin)
            else:
                print(registereddata.errors)
            
    return render(request,'admin/adminregistration.html')


@csrf_exempt
def adminLogin(request):
    if request.method=="POST":
        print(1)
        getusername=request.POST.get('eusername')
        getpassword=request.POST.get('epassword')
        flag=0
        data=AdminloginModel.objects.filter(eusername=getusername,epassword=getpassword)
        print(data)
        if data:
            adminserialiser=AdminloginSerializer(data,many=True)
            request.session['user']=adminserialiser.data
            print(request.session['user'])
            a="adminLogin"
            return redirect(adminheader)
    return render(request,'admin/adminlogin.html')


def adminlogout(request):
    if request.session.has_key('user'):
        del request.session['user']
    if request.session.has_key('currentplan'):
        del request.session['currentplan']
    return redirect(adminhomepage)


# @csrf_exempt
# def addlogin(request):
#     if(request.method == "POST"):
#         mydata = JSONParser().parse(request)
#         login_serializer = loginSerializer(data=mydata)
#         if(login_serializer.is_valid()):
#             login_serializer.save()
#             print("YES")
#             return HttpResponse("OK")
#         else:
#             return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)

def adminheader(request):
    return render(request,'admin/adminheader.html')
###########################    mobile prepaid   #########################
@csrf_exempt
def update_prepaidplans(request):
    getId=request.POST.get("newid")
    getplanname=request.POST.get("newplanname")
    getvalidity=request.POST.get("newvalidity")
    getpdata=request.POST.get("newpdata")
    gettalktime=request.POST.get("newtalktime")
    getsms=request.POST.get("newsms")
    getptype=request.POST.get("newptype")
    mydata={'pname':getplanname,'pvalidity':getvalidity,'pdata':getpdata,'ptalktime':gettalktime,'psms':getsms,'ptype':getptype}
    plandata=PrepaidMobilePlansModel.objects.get(id=getId)
    plandataserializer=PrepaidMobilePlansSerializer(plandata,data=mydata)
    print(plandataserializer)
    if plandataserializer.is_valid():
        plandataserializer.save()
    else:
        print(plandataserializer.errors())
    
    return redirect(viewallmprepaid)

@csrf_exempt
def mobileprepaid_details(request,fetchid):
    try:
        mprepaid=PrepaidMobilePlansModel.objects.get(id=fetchid)
        if(request.method=="GET"):
            mprepaid_serializer=PrepaidMobilePlansSerializer(mprepaid)
            return JsonResponse(mprepaid_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydata1=JSONParser().parse(request)
            mprepaid_serialize=PrepaidMobilePlansSerializer(mprepaid,data=mydata1)
            if(mprepaid_serialize.is_valid()):
                mprepaid_serialize.save()
                return JsonResponse(mprepaid_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(mprepaid_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except PrepaidMobilePlansModel.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_mprepaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PrepaidMobilePlansModel.objects.filter(ptype=getptype)
        mprepaid_serialize=PrepaidMobilePlansSerializer(getplantype,many=True)
        return render(request,"admin/prepaidupdate.html",{"data":mprepaid_serialize.data})
    except:   
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 

def updateprepaid(request):
    return render(request,'admin/prepaidupdate.html') 

@csrf_exempt
def mprepaid_list(request):
    if(request.method=="GET"):
        mprepaid=PrepaidMobilePlansModel.objects.all()
        mprepaid_serializer=PrepaidMobilePlansSerializer(mprepaid,many=True)
        return JsonResponse(mprepaid_serializer.data,safe=False)
def viewallmprepaid(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewmprepaid").json()
    return render(request,'admin/viewmprepaid.html',{"data":fetchdata})

#####################   dongle prepaid ##############################

@csrf_exempt
def update_prepaiddongleplans(request):
    getId=request.POST.get("newid")
    getplanname=request.POST.get("newplanname")
    getvalidity=request.POST.get("newvalidity")
    getpdata=request.POST.get("newpdata")
    gettalktime=request.POST.get("newtalktime")
    getptype=request.POST.get("newptype")
    mydata={'pname':getplanname,'pvalidity':getvalidity,'pdata':getpdata,'ptalktime':gettalktime,'ptype':getptype}
    plandata=PrepaidDonglePlansModel.objects.get(id=getId)
    plandataserializer=PrepaidDonglePlansSerializer(plandata,data=mydata)
    print(plandataserializer)
    if plandataserializer.is_valid():
        plandataserializer.save()
    else:
        print(plandataserializer.errors())
    
    return redirect(viewalldprepaid)

@csrf_exempt
def dongleprepaid_details(request,fetchid):
    try:
        dprepaid=PrepaidDonglePlansModel.objects.get(id=fetchid)
        if(request.method=="GET"):
            dprepaid_serializer=PrepaidDonglePlansSerializer(dprepaid)
            return JsonResponse(dprepaid_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydata1=JSONParser().parse(request)
            dprepaid_serialize=PrepaidDonglePlansSerializer(dprepaid,data=mydata1)
            if(dprepaid_serialize.is_valid()):
                dprepaid_serialize.save()
                return JsonResponse(dprepaid_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(dprepaid_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except PrepaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_dprepaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PrepaidDonglePlansModel.objects.filter(ptype=getptype)
        dprepaid_serialize=PrepaidDonglePlansSerializer(getplantype,many=True)
        return render(request,"admin/dongleprepaidupdate.html",{"data":dprepaid_serialize.data})
    except:   
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 

def updatedprepaid(request):
    return render(request,'admin/dongleprepaidupdate.html') 

@csrf_exempt
def dprepaid_list(request):
    if(request.method=="GET"):
        dprepaid=PrepaidDonglePlansModel.objects.all()
        dprepaid_serializer=PrepaidDonglePlansSerializer(dprepaid,many=True)
        return JsonResponse(dprepaid_serializer.data,safe=False)
def viewalldprepaid(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewdprepaid").json()
    return render(request,'admin/viewdprepaid.html',{"data":fetchdata})
######################### dongle postpaid ######################

@csrf_exempt
def update_postpaiddongleplans(request):
    getId=request.POST.get("newid")
    getplanname=request.POST.get("newplanname")
    getvalidity=request.POST.get("newvalidity")
    getpdata=request.POST.get("newpdata")
    getptype=request.POST.get("newptype")
    getsms=request.POST.get("newsms")
    getsubscription=request.POST.get("newsubscription")
    mydata={'pname':getplanname,'pvalidity':getvalidity,'pdata':getpdata,'ptype':getptype,'sms':getsms,'subscription':getsubscription}
    plandata=PostpaidDonglePlansModel.objects.get(id=getId)
    plandataserializer=PostpaidDonglePlansSerializer(plandata,data=mydata)
    print(plandataserializer)
    if plandataserializer.is_valid():
        plandataserializer.save()
    else:
        print(plandataserializer.errors())
    
    return redirect(viewalldpostpaid)



@csrf_exempt
def donglepostpaid_details(request,fetchid):
    try:
        dpostpaid=PostpaidDonglePlansModel.objects.get(id=fetchid)
        if(request.method=="GET"):
            dpostpaid_serializer=PostpaidDonglePlansSerializer(dpostpaid)
            return JsonResponse(dpostpaid_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydata1=JSONParser().parse(request)
            dpostpaid_serialize=PostpaidDonglePlansSerializer(dpostpaid,data=mydata1)
            if(dpostpaid_serialize.is_valid()):
                dpostpaid_serialize.save()
                return JsonResponse(dpostpaid_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(dpostpaid_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except PostpaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_dpostpaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PostpaidDonglePlansModel.objects.filter(ptype=getptype)
        dpostpaid_serialize=PostpaidDonglePlansSerializer(getplantype,many=True)
        return render(request,"admin/donglepostpaidupdate.html",{"data":dpostpaid_serialize.data})
    except:   
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 

def updatedpostpaid(request):
    return render(request,'admin/donglepostpaidupdate.html') 

@csrf_exempt
def dpostpaid_list(request):
    if(request.method=="GET"):
        dpostpaid=PostpaidDonglePlansModel.objects.all()
        dpostpaid_serializer=PostpaidDonglePlansSerializer(dpostpaid,many=True)
        return JsonResponse(dpostpaid_serializer.data,safe=False)
def viewalldpostpaid(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewdpostpaid").json()
    return render(request,'admin/viewdpostpaid.html',{"data":fetchdata})

######################### mobile postpaid ######################

@csrf_exempt
def update_postpaidmplans(request):
    getId=request.POST.get("newid")
    getplanname=request.POST.get("newplanname")
    getpdata=request.POST.get("newpdata")
    getsms=request.POST.get("newsms")
    getcalls=request.POST.get("newcalls")
    getsubscription=request.POST.get("newsubscription")
    mydata={'plan_name':getplanname,'data':getpdata,'calls':getcalls,'SMS':getsms,'subs':getsubscription}
    plandata=PlanPostpaidMobile.objects.get(id=getId)
    plandataserializer=PlanSerializerpost(plandata,data=mydata)
    print(plandataserializer)
    if plandataserializer.is_valid():
        plandataserializer.save()
    else:
        print(plandataserializer.errors())
    
    return redirect(viewallmpostpaid)



@csrf_exempt
def mpostpaid_details(request,fetchid):
    try:
        mpostpaid=PlanPostpaidMobile.objects.get(id=fetchid)
        if(request.method=="GET"):
            mpostpaid_serializer=PlanSerializerpost(mpostpaid)
            return JsonResponse(mpostpaid_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydata1=JSONParser().parse(request)
            mpostpaid_serialize=PlanSerializerpost(mpostpaid,data=mydata1)
            if(mpostpaid_serialize.is_valid()):
                mpostpaid_serialize.save()
                return JsonResponse(mpostpaid_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(mpostpaid_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except PlanPostpaidMobile.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_mpostpaid(request):
    try:
        getplanname=request.POST.get("plan_name")
        getplannames=PlanPostpaidMobile.objects.filter(plan_name=getplanname)
        mpostpaid_serialize=PlanSerializerpost(getplannames,many=True)
        return render(request,"admin/mobilepostpaidupdate.html",{"data":mpostpaid_serialize.data})
    except:   
        return HttpResponse("Invalid planname",status=status.HTTP_404_NOT_FOUND) 

def updatempostpaid(request):
    return render(request,'admin/mobilepostpaidupdate.html') 

@csrf_exempt
def mpostpaid_list(request):
    if(request.method=="GET"):
        mpostpaid=PlanPostpaidMobile.objects.all()
        mpostpaid_serializer=PlanSerializerpost(mpostpaid,many=True)
        return JsonResponse(mpostpaid_serializer.data,safe=False)
def viewallmpostpaid(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewmpostpaid").json()
    return render(request,'admin/viewmobilepostpaid.html',{"data":fetchdata})




########################### SEARCH #################################

################# MOBILE PREPAID SEARCH ############################

def mobprepaidsearch(request):
    return render(request,'admin/prepaidsearch.html')

@csrf_exempt
def mobpresearch(request,fetchid):
    try:
        mobpre=PrepaidMobilePlansModel.objects.get(id=fetchid)
        if(request.method == "GET"):
            Mobpre_Serializer=PrepaidMobilePlansSerializer(mobpre)
            return JsonResponse(Mobpre_Serializer.data,safe=False,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serislixation")
    except PrepaidMobilePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def mobpresearchapi(request):
    try:
        getMobpre=request.POST.get("ptype")
        getmobpre=PrepaidMobilePlansModel.objects.filter(ptype=getMobpre)
        Mobpre_Serializer=PrepaidMobilePlansSerializer(getmobpre,many=True)
        return render(request,"admin/prepaidsearch.html",{"data":Mobpre_Serializer.data})
       
    except PrepaidMobilePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan Type",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")

############################ MOBILE POSTPAID SEARCH ####################

def mobpostpaidsearch(request):
    return render(request,'admin/postpaidsearch.html')

@csrf_exempt
def mobpostsearch(request,fetchid):
    try:
        mobpost=PlanPostpaidMobile.objects.get(id=fetchid)
        if(request.method == "GET"):
            Mobpost_Serializer=PlanSerializerpost(mobpost)
            return JsonResponse(Mobpost_Serializer.data,safe=False,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serislization")
    except PlanPostpaidMobile.DoesNotExist:
        return HttpResponse("Invalid Plan",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def mobpostsearchapi(request):
    try:
        getMobpost=request.POST.get("plan_name")
        getmobpost=PlanPostpaidMobile.objects.filter(plan_name=getMobpost)
        Mobpost_Serializer=PlanSerializerpost(getmobpost,many=True)
        return render(request,"admin/postpaidsearch.html",{"data":Mobpost_Serializer.data})
       
    except PlanPostpaidMobile.DoesNotExist:
        return HttpResponse("Invalid Plan Type",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")

######################## DONGLE POSTPAID SEARCH ##########################

def donglepostpaidsearch(request):
    return render(request,'admin/donglepostpaidsearch.html')

@csrf_exempt
def donglepostsearch(request,fetchid):
    try:
        Donglepost=PostpaidDonglePlansModel.objects.get(id=fetchid)
        if(request.method == "GET"):
            Donglepost_Serializer=PostpaidDonglePlansSerializer(Donglepost)
            return JsonResponse(Donglepost_Serializer.data,safe=False,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serislization")
    except PostpaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def donglepostsearchapi(request):
    try:
        getDonglepost=request.POST.get("ptype")
        getdonglepost=PostpaidDonglePlansModel.objects.filter(ptype=getDonglepost)
        Donglepost_Serializer=PostpaidDonglePlansSerializer(getdonglepost,many=True)
        return render(request,"admin/donglepostpaidsearch.html",{"data":Donglepost_Serializer.data})
       
    except PostpaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan Type",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")


######################## DONGLE PREPAID SEARCH ##########################

def dongleprepaidsearch(request):
    return render(request,'admin/dongleprepaidsearch.html')

@csrf_exempt
def donglepresearch(request,fetchid):
    try:
        Donglepre=PrepaidDonglePlansModel.objects.get(id=fetchid)
        if(request.method == "GET"):
            Donglepre_Serializer=PrepaidDonglePlansSerializer(Donglepre)
            return JsonResponse(Donglepre_Serializer.data,safe=False,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization")
    except PrepaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def donglepresearchapi(request):
    try:
        getDonglepre=request.POST.get("ptype")
        getdonglepre=PrepaidDonglePlansModel.objects.filter(ptype=getDonglepre)
        Donglepre_Serializer=PrepaidDonglePlansSerializer(getdonglepre,many=True)
        return render(request,"admin/dongleprepaidsearch.html",{"data":Donglepre_Serializer.data})
       
    except PrepaidDonglePlansModel.DoesNotExist:
        return HttpResponse("Invalid Plan Type",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")



#################### DELETE########################
############### MOBILE PREPAID DELETE ############

def deleteprepaid(request):
    return render(request,'admin/prepaiddelete.html') 


@csrf_exempt
def delete_prepaidplans(request):
    getId=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/voice/viewprepaid/"+getId 
    requests.delete(Apilink)
    # return HttpResponse("Data has deleted successfully") 
    return redirect(viewallmprepaid)       
    
    

@csrf_exempt
def delete_search_mprepaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PrepaidMobilePlansModel.objects.filter(ptype=getptype)
        mprepaid_serialize=PrepaidMobilePlansSerializer(getplantype,many=True)
        return render(request,"admin/prepaiddelete.html",{"data":mprepaid_serialize.data})
    except PrepaidMobilePlansModel.DoesNotExist:  
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("Something is Wrong")


############### MOBILE POSTPAID DELETE ############

def deletepostpaid(request):
    return render(request,'admin/postpaiddelete.html') 


@csrf_exempt
def delete_postpaidplans(request):
    getId=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/voice/viewprepaid/"+getId 
    requests.delete(Apilink)
    # return HttpResponse("Data has deleted successfully") 
    return redirect(viewallmprepaid)       
    
    

@csrf_exempt
def delete_search_mpostpaid(request):
    try:
        getptype=request.POST.get("plan_name")
        getplantype=PlanPostpaidMobile.objects.filter(plan_name=getptype)
        mprepaid_serialize=PlanSerializerpost(getplantype,many=True)
        return render(request,"admin/postpaiddelete.html",{"data":mprepaid_serialize.data})
    except PlanPostpaidMobile.DoesNotExist:  
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("Something is Wrong")



############### DONGLE PREPAID DELETE ############

def deleteprepaiddongle(request):
    return render(request,'admin/dongleprepaiddelete.html') 


@csrf_exempt
def delete_dongleprepaidplans(request):
    getId=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/voice/viewdprepaid/"+getId 
    requests.delete(Apilink)
    # return HttpResponse("Data has deleted successfully") 
    return redirect(viewallmprepaid)       
    
    

@csrf_exempt
def delete_search_dongleprepaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PrepaidDonglePlansModel.objects.filter(ptype=getptype)
        dongleprepaid_serialize=PrepaidDonglePlansSerializer(getplantype,many=True)
        return render(request,"admin/dongleprepaiddelete.html",{"data":dongleprepaid_serialize.data})
    except PrepaidDonglePlansModel.DoesNotExist:  
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("Something is Wrong")


############### DONGLE POSTPAID DELETE ############

def deletepostpaiddongle(request):
    return render(request,'admin/donglepostpaiddelete.html') 


@csrf_exempt
def delete_donglepostpaidplans(request):
    getId=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/voice/viewdprepaid/"+getId 
    requests.delete(Apilink)
    # return HttpResponse("Data has deleted successfully") 
    return redirect(viewallmprepaid)       
    
    

@csrf_exempt
def delete_search_donglepostpaid(request):
    try:
        getptype=request.POST.get("ptype")
        getplantype=PostpaidDonglePlansModel.objects.filter(ptype=getptype)
        donglepostpaid_serialize=PostpaidDonglePlansSerializer(getplantype,many=True)
        return render(request,"admin/donglepostpaiddelete.html",{"data":donglepostpaid_serialize.data})
    except PostpaidDonglePlansModel.DoesNotExist:  
        return HttpResponse("Invalid ptype",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("Something is Wrong")


##################### view all customers #############
@csrf_exempt
def customer_list(request):
    if(request.method=="GET"):
        customer=RegisterModel.objects.all()
        customer_serializer=RegisterSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)

def viewall_customers(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewallcustomers").json()
    return render(request,'admin/viewallcustomers.html',{"data":fetchdata})

def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')



###DONGLE DEVICE ####

def dongle(request):
    return render(request,'Dongle.html')

def dongregister(request):
    return render(request,'DONGLE/Registerdongle.html')

def dongsuccess(request):
    return render(request,'DONGLE/regisuccessdong.html')

def dongdashhead(request):
    return render(request,'Dongledashboard.html')
@csrf_exempt
def addcontact(request):
    if (request.method=="POST"):
        # dict1=JSONParser().parse(request)
        # result=json.dumps(dict1)
        # print(result)
        contactserializer=contactSerializer(data=request.POST)
        if (contactserializer.is_valid()):
            print(1)
            contactserializer.save()
            return JsonResponse(contactserializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_404_NOT_FOUND) 
    else:
        return HttpResponse("Get method not allowed")

def regidongdash(request):
    return render(request,'DONGLE/registerdash.html')


@csrf_exempt
def dongcustomer_list(request):
    if(request.method=="GET"):
        customer=Dongleregister.objects.all()
        customer_serializer=DongleregiSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)
def viewdongle(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voice/viewdongcust").json()
    return render(request,'admin/viewdonglecustomer.html',{"data":fetchdata})



@csrf_exempt
def dong_regiadd(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        # dong_serializer = DongleregiSerializer(data=mydata)
        dong_serializer = DongleregiSerializer(data=request.POST)
        if(dong_serializer.is_valid()):
            dong_serializer.save()
            messages.success(request, 'Dongle Registerd')
            # return JsonResponse(dong_serializer.data,safe=False,status=status.HTTP_200_OK)
            return redirect(dongsuccess)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)




def queryview(request):
    fetchdata = requests.get("http://127.0.0.1:8000/voice/query").json()
    return render(request,'admin/query.html',{"data":fetchdata})
    
@csrf_exempt
def query_list(request):
    if(request.method=="GET"):
        query=contactModel.objects.all()
        query_serializer=contactSerializer(query,many=True)
        return JsonResponse(query_serializer.data,safe=False)

@csrf_exempt
def adminbill(request):
    data=RegisterModel.objects.all()
    if request.method=="POST":
        id=request.POST.get('cid')
        print(id)
        billdata=BillManagementModel.objects.filter(cid=id)
        print(billdata)
        return render(request,'admin/adminbill.html',{'bill':billdata})
    return render(request,'admin/adminbill.html',{'data':data})





#<li><a class="btn btn-secondary" href="http://127.0.0.1:8000/voice/viewdong">VIEW DONGLE CUSTOMERS</a></li>
