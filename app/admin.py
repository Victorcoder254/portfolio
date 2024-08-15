from django.contrib import admin
from .models import *


class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "location")


admin.site.register(Visitor, VisitorAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ("name", "updated")


admin.site.register(About, AboutAdmin)


class FootInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "updated")


admin.site.register(FooterInfo, FootInfoAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")


admin.site.register(Skill, SkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(Project, ProjectAdmin)