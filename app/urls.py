from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('metrics/', visitor_metrics, name='visitor_metrics'),
]