from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    ROLE_CHOICES = [
        ('employee', 'Looking for Work (Employee)'),
        ('employer', 'Hiring Staff (Employer)'),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Account Type"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')

        if role == 'employee':
            user.type = "Employee"
        elif role == 'employer':
            user.type = "Employer"

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
