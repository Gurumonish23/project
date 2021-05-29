from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from portal.models.univdetail import Univdetail,Univcon
from portal.models.studentinfo import Student
from portal.models.universityinfo import University
from django.contrib.auth.hashers import make_password,check_password
from portal.models.stddetail import Stdacd,Stdcour,Stdpro,Stdpro1,Stdind
from portal.models.stdappli import Stdappli
from portal.models.courses import Courses
from portal.models.application import Application

def Home(request):
    return render(request,'super_admin/home.html')
def Courses(request):
    return render(request,'super_admin/courses.html')
def Settings(request):
    return render(request,'super_admin/settings.html')
def students(request):
    stddetail=Stdappli.objects.all()
    data={}
    data['stddetail']=stddetail
    #return render(request,'.html',data)
    return render(request,'super_admin/students.html',data)
def universities(request):
    return render(request,'super_admin/universities.html')
def agent(request):
    return render(request,'super_admin/agents.html')
def single_university(request):
    return render(request,'super_admin/single_university.html')
def single_agent(request):
    return render(request,'super_admin/single_agent.html')
