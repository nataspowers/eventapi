from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('api/', views.EventList.as_view(), name='event-list'),
    path('api/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
