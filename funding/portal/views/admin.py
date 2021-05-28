from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View

def Home(request):
    return render(request,'super_admin/home.html')
def Courses(request):
    return render(request,'super_admin/courses.html')
def Settings(request):
    return render(request,'super_admin/settings.html')
def students(request):
    return render(request,'super_admin/students.html')
def universities(request):
    return render(request,'super_admin/universities.html')
def agent(request):
    return render(request,'super_admin/agents.html')
def single_university(request):
    return render(request,'super_admin/single_university.html')
def single_agent(request):
    return render(request,'super_admin/single_agent.html')
