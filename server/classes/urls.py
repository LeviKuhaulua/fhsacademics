from django.urls import path
from .views import listAps, apClassDetail 

urlpatterns = [
    path('', listAps, name='all_aps'),
    path('<slug:class_name>', apClassDetail, name='specific_ap')
]