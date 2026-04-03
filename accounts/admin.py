from django.contrib import admin
from .models import User
from .forms import SignUpForm, LoginForm

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Information about the user", {
            "fields": ["first_name", "last_name", "username", "email","type"]
        }),
    ]

    list_display = ["username", "email", "first_name", "last_name"]
    list_filter = ["username", "email"]
    search_fields = ["username", "email"]

admin.site.register(User, UserAdmin)
