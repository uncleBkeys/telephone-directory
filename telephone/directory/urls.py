from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('', amendpage, name='amendpage'),
    path('', insertpage, name='insertpage'),
    path('', removepage, name='removepage'),


]
