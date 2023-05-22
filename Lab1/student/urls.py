from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', listStudent),
    path('insert/', insertStudent),
    path('update/', updateStudent),
    path('delete/', deleteStudent),
]
