from django.urls import path
from .views import ApClassList, ApClassDetail
from .views import EventList, EventDetail
urlpatterns = [
    path('classes/', ApClassList.as_view(), name='all_aps'),
    path('classes/<slug:slug>', ApClassDetail.as_view(), name='specific_ap'),
    path('events/', EventList.as_view(), name='all_events'),
    path('events/<int:id>', EventDetail.as_view(), name='specific_event'),
]