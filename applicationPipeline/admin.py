from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "get_company", "applicant", "status", "created_at")
    list_filter = ("status", "job__company")

    def get_company(self, obj):
        return obj.job.company
    get_company.short_description = "Company"

