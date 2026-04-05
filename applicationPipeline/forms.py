from django import forms
from .models import Application

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["status", "notes", "contact_person", "deadline"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
