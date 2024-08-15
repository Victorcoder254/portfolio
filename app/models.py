from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"


class About(models.Model):
    name = models.CharField(max_length=100 ,blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/',blank=True, null=True)
    family_background = models.TextField(blank=True, null=True)
    academic_background = models.TextField(blank=True, null=True)
    self_learning_journey = models.TextField(blank=True, null=True)
    thoughts_on_ai = models.TextField(blank=True, null=True)
    entrepreneurial_aspirations = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "About Information"
    

class FooterInfo(models.Model):
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Footer Information"
    
class Skill(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)  # e.g., Beginner, Intermediate, Expert

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)  # Link to the project

    def __str__(self):
        return self.title    