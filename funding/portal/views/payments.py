from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
import stripe
#from stripe import response
from django.conf import settings
from portal.models.stdappli import Stdappli

stripe.api_key=settings.STRIPE_SECRET_KEY   

'''def get_context_data(self,**kwargs):
    context=super().get_context_data(**kwargs)
    context['key']=settings.STRIPE_PUBLISHABLE_KEY
    return context'''

def payment(request,name="a",name1="b"):
    value={}
    value['id']=name
    value['fee']=name1
    print(name1)
    print(value['fee'])
    value['key']=settings.STRIPE_PUBLISHABLE_KEY


    return render(request,'payment.html',{'value':value})

def charge(request,name="a",name1='b'):
    print(name)
    print("nanda")
    if request.method=='POST':
        print("kishore")
        charge=stripe.Charge.create(
            amount=int(name)*100,
            currency='inr',
            description='Application Payment',
            source=request.POST['stripeToken']
        )
        #print(amount)
        print("nanad")
        print(charge.amount)
        print(charge.status)
        
        stdappli=Stdappli.objects.get(id=name1)
        stdappli.pstatus=charge.status
        stdappli.save()
        value={}
        value['status']=charge.status
        try:
            if(request.session['email2']):
                value['path']="/agent/home"
        except:
            value['path']="/student/home"
        return render(request,'charge.html',{'value':value})
       








