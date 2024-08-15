from django.shortcuts import render, get_object_or_404# Ensure this template existsfrom django.shortcuts import render, get_object_or_404
from .models import *
from app.models import *  # Import About model

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created')
    about_info = About.objects.first()
    footer_info = FooterInfo.objects.first()  # Fetch the first instance of FooterInfo
    
    context = {
        'about_info': about_info,
        'posts': posts,
        'footer_info': footer_info,
    }
    return render(request, 'files/home_blog.html', context)

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    about_info = About.objects.first()
    footer_info = FooterInfo.objects.first()  # Fetch the first instance of FooterInfo

    context = {
        'about_info': about_info,
        'post': post,
        'footer_info': footer_info,
    }
    return render(request, 'files/detail.html', context)
