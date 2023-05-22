from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', links),
    path('students/', listStudent),
    path('staffs/', listStaff),

]
