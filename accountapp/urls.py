from django.contrib import admin
from django.urls import path

from accountapp.views import hi_nini

app_name = 'accountapp'

urlpatterns = [
    path('hi_nini/', hi_nini, name='aloha')
]