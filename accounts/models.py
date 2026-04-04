from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TYPE_CHOICES = [
        ("Employer", "Employer"),
        ("Employee", "Employee"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.username

    @property
    def is_employee(self):
        return self.type == "Employee"

    @property
    def is_employer(self):
        return self.type == "Employer"

