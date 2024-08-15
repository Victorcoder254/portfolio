from django.contrib import admin
from .models import*

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone')
