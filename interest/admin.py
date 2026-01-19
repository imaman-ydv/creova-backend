from django.contrib import admin
from .models import InterestSubmission

@admin.register(InterestSubmission)
class InterestSubmissionAdmin(admin.ModelAdmin):
    list_display = ('interest','price','email','ip_address','created_at')
    list_filter = ('interest','created_at')
    search_fields = ('email','ip_address')
    readonly_fields = ('ip_address','created_at')
