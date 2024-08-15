from django.shortcuts import render
from .models import *


def home_view(request):
    about_info = About.objects.first()
    footer_info = FooterInfo.objects.first()  # Fetch the first instance of FooterInfo
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'about_info': about_info,
        'skills': skills,
        'projects': projects,
        'footer_info': footer_info,
    }

    return render(request, 'files/home.html', context)

def visitor_metrics(request):
    total_visitors = Visitor.objects.count()
    visitors = Visitor.objects.all().order_by('-visit_date')
    about_info = About.objects.first()
    footer_info = FooterInfo.objects.first()  # Fetch the first instance of FooterInfo
    
    context = {
        'total_visitors': total_visitors,
        'visitors': visitors,
        'footer_info': footer_info,
        'about_info': about_info,
    }
    return render(request, 'files/metrics.html', context)