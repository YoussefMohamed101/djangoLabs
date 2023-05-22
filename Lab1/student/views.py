from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def listStudent(r):
    return HttpResponse("listed students")

def insertStudent(r):
    return render(r,'student/insert.html')

def updateStudent(r):
    return render(r,'student/update.html')

def deleteStudent(r):
    return HttpResponseRedirect('/student')