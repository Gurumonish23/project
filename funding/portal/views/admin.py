from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from portal.models.univdetail import Univdetail,Univcon
from portal.models.consultancyinfo import Consultancy
from portal.models.studentinfo import Student
from portal.models.universityinfo import University
from django.contrib.auth.hashers import make_password,check_password
from portal.models.stddetail import Stdacd,Stdcour,Stdpro,Stdpro1,Stdind
from portal.models.stdappli import Stdappli
from portal.models.coursecommision import Coursecommision

from portal.models.courses import Courses
from portal.models.application import Application
def Home(request):
    return render(request,'super_admin/home.html')
#def Courses(request):
#    return render(request,'super_admin/courses.html')
def Settings(request):
    return render(request,'super_admin/settings.html')
def students(request):
    stddetail=Stdappli.objects.all()
    data={}
    data['stddetail']=stddetail
    #return render(request,'.html',data)
    return render(request,'super_admin/students.html',data)
def universities(request):
    university1=University.objects.all()
    data={}
    list=[]
    list1=[]
    name=[]
    phone=[]
    country=[]
    email=[]
    rank=[]
    award=[]
    for i in university1:
       list.extend([[i.Firstname,i.Email]])

    for i in range(0,len(list)):
        name.append(list[i][0])
        email.append(list[i][1])
        phone.append(University.objects.get(Firstname=list[i][0]).Phonenumber)
        country.append(Univcon.objects.get(Email=list[i][1]).Location)
        rank.append(Univdetail.objects.get(Email=list[i][1]).Rank)
        award.append(Univcon.objects.get(Email=list[i][1]).Award)
        #detail[name]={'name':name,'award':award,'country':country,'rank':rank,'email':email,'phone':phone}
    for i in range(0,len(list)):
                list1.append({'name':name[i],
                         'email':email[i],
                              'phone':phone[i],
                                'country':country[i],'rank':rank[i],'award':award[i]})    
                                                      
        #print(detail[name])
    data['detail']=list1
    return render(request,'super_admin/universities.html',data)
def agent(request):
    agent=Consultancy.objects.all()
    data={}
    data['agent']=agent
    return render(request,'super_admin/agents.html',data)
def single_university(request):
    return render(request,'super_admin/single_university.html')
def single_agent(request):
    return render(request,'super_admin/single_agent.html')
class commision(View):
    def get(self,request):
        university=University.objects.all()
        data={}
        data['university']=university        
        return render(request,'super_admin/commision.html',data)
    def post(self,request):
        uniname=request.POST.get('uniname')
        value={}
        data={}
        value['uniname']=uniname
        data['value']=value
        return render(request,'super_admin/commision.html',data)
class addcommision(View):
    def get(self,request,name="a"):
        university=University.objects.get(Firstname=name)
        print(university.Email)
        courses1=Courses.objects.filter(Email=university.Email)
        print(courses1)
        data={}
        data['courses1']=courses1
        data['uniname']=name
        return render(request,'super_admin/addcommision.html',data)

    def post(self,request,name="a"):
        unimail=University.objects.get(Firstname=name).Email
        name1=request.POST.getlist('name[]')
        curr=request.POST.getlist('curr[]')
        amo=request.POST.getlist('amo[]')
        com=request.POST.getlist('com[]')
        for i in range(0,len(name1)):
            commision=Coursecommision(Uniname=name,Unimail=unimail,Coursename=name1[i],
            Coursecurr=curr[i],Courseamo=amo[i],Coursecomm=com[i])
            commision1=False
            try:
                commision1=Coursecommision.objects.filter(Unimail=unimail).get(Coursename=name1[i])
            except:
                pass
            if(commision1):
                commision1.delete()
            commision.register()
            course1=Courses.objects.filter(Email=unimail).get(Name=name1[i])
            course1.com=com[i]
            course1.register()
        
        courses1=Courses.objects.filter(Email=unimail)
        print(courses1)
        data={}
        data['courses1']=courses1
        data['uniname']=name
        return render(request,'super_admin/addcommision.html',data)
