from django.contrib import admin
from django.urls import path

from accountapp.views import hi_nini

urlpatterns = [
    path('hi_nini/',hi_nini,name='aloha')
]