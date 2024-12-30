from django.urls import path
from .views import ApClassList, ApClassDetail

urlpatterns = [
    path('classes/', ApClassList.as_view(), name='all_aps'),
    path('classes/<slug:slug>', ApClassDetail.as_view(), name='specific_ap')
]