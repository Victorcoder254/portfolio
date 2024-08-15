from django.urls import path
from .views import *


urlpatterns = [
    path('', contact_view, name='contact'),  # Name the URL 'blog'
    path('success/', contact_success_view, name='contact-success'),
]