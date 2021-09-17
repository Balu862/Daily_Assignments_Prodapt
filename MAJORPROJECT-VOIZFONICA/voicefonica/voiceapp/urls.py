from .import views
from django.urls import path

urlpatterns=[
    path('addplan/',views.addplan,name='add'),
    path('',views.home,name="home"),
    path("homeprepaid",views.homeprepaid,name="homeprepaid"),
    path("truleyunlimted",views.truelyunlimeted,name="truelyunlimeted"),
    path("intlr",views.intlr,name="intlr"),
    path("smartrecharge",views.smartrecharge,name="smartrecharge"),
    path("talktime",views.talktime,name="talktime"),
    path("data",views.data,name="talktime"),
    path('login',views.Login,name="login"),
    path('register',views.Registration,name="registration"),
    path('index',views.Index,name="index"),
    path('prepaid',views.Prepaid,name="index"),
    path('head',views.head,name="header"),
    path("ddata",views.ddata,name="ddata"),
    path("dintlr",views.dintlr,name="intlr"),
    path("dsmartrecharge",views.dsmartrecharge,name="smartrecharge"),
    path("dtalktime",views.dtalktime,name="talktime"),
    path("dtruleyunlimted",views.dtruelyunlimeted,name="truelyunlimeted"),
    path("addprepaid",views.prepaidcustomer,name="prepaidcustomer"),
    path("paymentpre",views.paymentpre,name="payment"),
    path("prepaidbill",views.BillManagement,name="bill"),
    path('billgeneration',views.billgeneration,name="billgeneration"),
    path("prepaidusage",views.usage,name="prepaidusage"),
    path("data/",views.data,name="data"),
    path("logout",views.logout,name="logout"),
    path('usage',views.usage,name="usage"),
    #postpaid mobile
    path('postplan/',views.planpostpaid,name="planpostpaid"),
    path('postview/',views.viewplanpost,name="viewplanpost"),
    path('viewone/<id>',views.view_oneplan,name='view_oneplan'),
    path('filldetail/',views.filldetailpost,name="filldetailpost"),
    path('detailshow/',views.detail_post_show,name="detail_post_show"),
    path('usageadd/',views.usage_add,name="usage_add"),
    path('usageview/',views.usage_view,name="usage_view"),
    path('accountadd/',views.account_add,name="account_add"),
    path('accountview/',views.account_view,name="account_view"),
    path('serviceadd/',views.service_add,name="service_add"),
    path('serviceview/',views.service_view,name="service_view"),
    path('monthadd/',views.monthly_add,name="monthly_add"),
    path('monthlyview/',views.monthly_view,name="monthly_view"),
   
    path('post/',views.postpage,name="postpage"),
    path('viewsui',views.view_mobile_post_plan,name="view_mobile_post_plan"),
    path('detailfill/',views.detail_fill_post,name="detail_fill_post"),
    path('bill/',views.billpaid,name="billpaid"),
    path('paypostpaid/',views.pay,name="pay"),
    path('dviewsui',views.dview_mobile_post_plan,name="dview_mobile_post_plan"),
    path('payment/',views.payment,name="payment"),
    path('submit/',views.submitpostpaid,name="submitpostpaid"),
    path('success/',views.successpost,name="successpost"),
    path('billpostpdf/',views.BillManagementpost,name="BillManagementpost"),
    path('cutomerviewpost/',views.viewpostcustomer,name="viewpostcustomer"),


   

   #postpaid dongle links
    path('addpostdongleplan/',views.addpostdongleplan,name='addpostdongleplan'), 
    path('postpaiddongle/',views.Postpaiddongle,name="Postpaiddongle"),
    path("postpaiddongleplan",views.postpaidDonglePlan,name="postpaidDonglePlan"),
    path("postpaiddongleb",views.PostpaidDonglecustomer,name="PostpaidDonglecustomer"),
    path('postpaidDdata',views.postpaidDdata,name="postpaidDdata"),
    path('postdongledata',views.postdongledata,name="postdongledata"),
    path('homepostpaiddongle',views.homepostpaiddongle,name="homepostpaiddongle"),
    path('postdongleplans',views.postdongleplans,name="postdongleplans"),

#prepaid dongle links
    path('addpredongleplan/',views.addpredongleplan,name='addpredongleplan'),
    path("prepaiddongleb",views.PrepaidDonglecustomer,name="PrepaidDonglecustomer"),
    path('trulydongleunlimited',views.trulydongleunlimeted,name="trulydongleunlimeted"),
    path("prepaiddongleplan",views.prepaiddongle,name="prepaidDonglePlan"),
    path('predongledata',views.predongledata,name="predongledata"),
    path('prepaiddongle',views.prepaidDonglePlan,name="prepaiddongle"),
    path('donglesmartrecharge',views.donglesmartrecharge,name="dsmartrecharge"),
    path('dongledata',views.dongledata,name="ddata"),
    path('homeprepaiddongle',views.homeprepaiddongle,name="homeprepaiddongle"),
    path('predongletruleyunlimted',views.predongletruleyunlimted,name="predongletruleyunlimted"),
    path('predonglesmartrecharge',views.predonglesmartrecharge,name="predonglesmartrecharge"),
    path('predongledata',views.predongledata,name="predongledata"),
    path("paymentpredong",views.paymentpredong,name="payment"),
    
#HELP DESK#
    path('faqhome',views.faqhome,name="faqhome"),
    path('faqposthome',views.faqposthome,name="faqposthome"),
    path('faqpostplan',views.faqpostplan,name="faqpostplan"),
    path('faqpostbill',views.faqpostbill,name="faqpostbill"),
    path('faqpostdata',views.faqpostdata,name="faqpostdata"),
    path('faqpostproduct',views.faqpostproduct,name="faqpostproduct"),
    path('faqpostactivate',views.faqpostactivate,name="faqpostactivate"),
    path('faqpostother',views.faqpostother,name="faqpostother"),
    path('faqprehome',views.faqprehome,name="faqprehome"),
    path('faqpregeneral',views.faqpregeneral,name="faqpregeneral"),
    path('faqpreproduct',views.faqpreproduct,name="faqpreproduct"),
    path('faqpredata',views.faqpredata,name="faqpredata"),
    path('faqdonghome',views.faqdonghome,name="faqdonghome"),
    path('faqdonggeneral',views.faqdonggeneral,name="faqdonggeneral"),
    
#help desk webpage#
    path('faqhomep',views.faqhomepage,name="faqhomepage"),
    path('faqposthomep',views.faqposthomepage,name="faqposthomepage"),
    path('faqpostplanp',views.faqpostplanpage,name="faqpostplanpage"),
    path('faqpostbillp',views.faqpostbillpage,name="faqpostbillpage"),
    path('faqpostdatap',views.faqpostdatapage,name="faqpostdatapage"),
    path('faqpostproductp',views.faqpostproductpage,name="faqpostproductpage"),
    path('faqpostactivatep',views.faqpostactivatepage,name="faqpostactivatepage"),
    path('faqpostotherp',views.faqpostotherpage,name="faqpostotherpage"),
    path('faqprehomep',views.faqprehomepage,name="faqprehomepage"),
    path('faqpregeneralp',views.faqpregeneralpage,name="faqpregeneralpage"),
    path('faqpreproductp',views.faqpreproductpage,name="faqpreproductpage"),
    path('faqpredatap',views.faqpredatapage,name="faqpredatapage"),
    path('faqdonghomep',views.faqdonghomepage,name="faqdonghomepage"),
    path('faqdonggeneralp',views.faqdonggeneralpage,name="faqdonggeneralpage"),
    
#admin
    # path('addlogin/',views.addlogin,name='addlogin'),
    path('adminheader',views.adminheader,name='adminheader'),
    path('adminRegistration',views.adminRegistration,name='adminRegistration'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('adminbill',views.adminbill,name="adminbill"),
    path('adminhomepage',views.adminhomepage,name='adminhomepage'),
    path('adminregistrationpage',views.adminregistrationpage,name='adminregistrationpage'),
    path('adminloginpage',views.adminloginpage,name='adminloginpage'),
    path('adminnhome',views.adminnhome,name='adminnhome'),


    
    ##############DELETE ###############################
    ###### MOBILE PREPAID ################
    path('deleteprepaid',views.deleteprepaid,name='deleteprepaid'),
    path('delete_search_mprepaid',views.delete_search_mprepaid,name='delete_search_mprepaid'),
    path('delete_api',views.delete_prepaidplans,name='delete_prepaidplans'),
    ###### MOBILE POSTPAID ################
    path('deletepostpaid',views.deletepostpaid,name='deletepostpaid'),
    path('delete_search_mpostpaid',views.delete_search_mpostpaid,name='delete_search_mpostpaid'),
    path('deletepostm_api',views.delete_postpaidplans,name='delete_postpaidplans'),
     ###### DONGLE PREPAID ################
    path('deleteprepaiddongle',views.deleteprepaiddongle,name='deleteprepaiddongle'),
    path('delete_search_dongleprepaid',views.delete_search_dongleprepaid,name='delete_search_dongleprepaid'),
    path('deletepred_api',views.delete_dongleprepaidplans,name='delete_dongleprepaidplans'),
    ###### DONGLE POSTPAID ################
    path('deletepostpaiddongle',views.deletepostpaiddongle,name='deletepostpaid'),
    path('delete_search_donglepostpaid',views.delete_search_donglepostpaid,name='delete_search_donglepostpaid'),
    path('deletepostd_api',views.delete_donglepostpaidplans,name='delete_donglepostpaidplans'),


    ############# SEARCH #################################
    ############# MOBILE PREPAID ##########################
    path('mobilepresearch/<fetchid>',views.mobpresearch,name='mobpresearch'),
    path('mobpresearchapi',views.mobpresearchapi,name='mobpresearchapi'),
    path('searchmobpre',views.mobprepaidsearch,name='mobprepaidsearch'),
    ############# MOBILE POSTPAID #########################
    path('mobilepostsearch/<fetchid>',views.mobpostsearch,name='mobpostsearch'),
    path('mobpostsearchapi',views.mobpostsearchapi,name='mobpostsearchapi'),
    path('searchmobpost',views.mobpostpaidsearch,name='mobpostpaidsearch'),
    ############# DONGLE POSTPAID ########################
    path('donglepostsearch/<fetchid>',views.donglepostsearch,name='donglepostsearch'),
    path('donglepostsearchapi',views.donglepostsearchapi,name='donglepostsearchapi'),
    path('searchdonglepost',views.donglepostpaidsearch,name='donglepostpaidsearch'),
    ############# DONGLE PREPAID ########################
    path('donglepresearch/<fetchid>',views.donglepresearch,name='donglepresearch'),
    path('donglepresearchapi',views.donglepresearchapi,name='donglepresearchapi'),
    path('searchdonglepre',views.dongleprepaidsearch,name='dongleprepaidsearch'),


#prepaidmobile
    path('viewprepaid/<fetchid>',views.mobileprepaid_details,name='mobileprepaid_details'),
    path('update_api',views.update_prepaidplans,name='update_prepaidplans'),
    path('update_search_mprepaid',views.update_search_mprepaid,name='update_search_mprepaid'),
    path('updatemprepaid',views.updateprepaid,name='updateprepaid'),
    path('viewallmprepaid/',views.viewallmprepaid,name='viewallmprepaid'),
    path('viewmprepaid',views.mprepaid_list,name='mprepaid_list'),
    path('mprepaidadd/',views.mprepaidadd,name='mprepaidadd'),
#prepaiddongle
    path('viewdprepaid/<fetchid>',views.dongleprepaid_details,name='dongleprepaid_details'),
    path('dupdate_api',views.update_prepaiddongleplans,name='update_prepaiddongleplans'),
    path('update_search_dprepaid',views.update_search_dprepaid,name='update_search_dprepaid'),
    path('updatedprepaid',views.updatedprepaid,name='updatedprepaid'),
    path('viewalldprepaid/',views.viewalldprepaid,name='viewalldprepaid'),
    path('viewdprepaid',views.dprepaid_list,name='dprepaid_list'),
    path('dprepaidadd',views.dprepaidadd,name='dprepaidadd'),

#postpaiddongle
    path('viewdpostpaid/<fetchid>',views.donglepostpaid_details,name='donglepostpaid_details'),
    path('postdupdate_api',views.update_postpaiddongleplans,name='update_postpaiddongleplans'),
    path('update_search_dpostpaid',views.update_search_dpostpaid,name='update_search_dpostpaid'),
    path('updatedpostpaid',views.updatedpostpaid,name='updatedpostpaid'),
    path('viewalldpostpaid/',views.viewalldpostpaid,name='viewalldpostpaid'),
    path('viewdpostpaid',views.dpostpaid_list,name='dpostpaid_list'),
    path('dpostpaidadd',views.dpostpaidadd,name='dpostpaidadd'),

#postpaidmobile
    path('viewmpostpaid/<fetchid>',views.mpostpaid_details,name='mpostpaid_details'),
    path('postmupdate_api',views.update_postpaidmplans,name='update_postpaidmplans'),
    path('update_search_mpostpaid',views.update_search_mpostpaid,name='update_search_mpostpaid'),
    path('updatempostpaid',views.updatempostpaid,name='updatempostpaid'),
    path('viewallmpostpaid/',views.viewallmpostpaid,name='viewallmpostpaid'),
    path('viewmpostpaid',views.mpostpaid_list,name='mpostpaid_list'),
    path('mpostadd',views.mpostadd,name='mpostadd'),

#viewall customers

    path('viewallcustomers',views.customer_list,name='customer_list'),
    path('viewcust',views.viewall_customers,name="viewall_customers"),

#dongle#
    
    path('dongle',views.dongle,name="dongle"),
    path('dongleregi',views.dongregister,name="dongregister"),
    path('dongsuccess',views.dongsuccess,name="dongsuccess"),
    path('dongdashead',views.dongdashhead,name="dongdashhead"),
    path('dongdashregi',views.regidongdash,name="regidongdash"),
    

    path('dongadd/',views.dong_regiadd,name="dong_regiadd"),
    path('viewdong',views.viewdongle,name="viewdongle"),
    path('viewdongcust',views.dongcustomer_list,name="viewdongle"),
    
    
    #about
    path('aboutus',views.aboutus,name="aboutus"),
    path('contact',views.addcontact,name="addcontact"),
    path('contactus',views.contactus,name="contactus"),
    path('query',views.query_list,name="query_list"),
    path('queryview',views.queryview,name="queryview"),

]