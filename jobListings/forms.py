from django import forms
from .models import JobListing

class JobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ["title", "content", "location", "salary_range"]
