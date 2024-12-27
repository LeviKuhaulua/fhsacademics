from django.urls import path
from .views import apClassList, apClassDetail 

urlpatterns = [
    path('', apClassList, name='all_aps'),
    path('<slug:class_name>', apClassDetail, name='specific_ap')
]