from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def listStudent(r):
    return HttpResponseRedirect('/student')

def listStaff(r):
    return HttpResponseRedirect('/staff')

def links(r):
    return render(r, 'report/links.html')