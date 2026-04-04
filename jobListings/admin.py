from django.contrib import admin
from .models import JobListing

class JobListingAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Information about the job", {
            "fields": ["title", "company", "level", "salary_range"]
        }),
        ("Location and type of work", {
            "fields": ["location", "work"]
        }),
        ("Content", {
            "fields": ["content"]
        }),
        ("Dates", {
            "fields": ["date_published"],
            "classes": ["collapse"]
        }),
    ]

    list_display = ["title", "company", "level", "location", "date_published"]
    list_filter = ["company", "level", "location", "date_published"]
    search_fields = ["title", "company__name", "location", "content"]

admin.site.register(JobListing, JobListingAdmin)
