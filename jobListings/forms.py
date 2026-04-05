from django import forms
from .models import JobListing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ["title", "level", "salary_range", "location", "work", "content"]
