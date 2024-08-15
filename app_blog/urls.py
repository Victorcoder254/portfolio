from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_view, name='blog'),  # Name the URL 'blog'
    path('<int:id>/', blog_detail, name='blog-detail'),
]