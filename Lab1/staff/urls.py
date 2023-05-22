from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', listStaff),
    path('insert/', insertStaff),
    path('update/', updateStaff),
    path('delete/', deleteStaff),
]
