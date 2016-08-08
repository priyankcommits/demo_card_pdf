from django.conf.urls import url, include
from django.contrib import admin
from democard.views import *

app_name = 'democard'
urlpatterns = [
    url(r'^$', card_pdf, name='card_pdf'),
]

