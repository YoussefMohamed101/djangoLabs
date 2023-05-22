from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def listStaff(r):
    return HttpResponse("listed staffs")

def insertStaff(r):
    return render(r, 'staff/insert.html')

def updateStaff(r):
    return render(r, 'staff/update.html')

def deleteStaff(r):
    return HttpResponseRedirect('/staff')