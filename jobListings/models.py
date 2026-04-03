from django.db import models
from datetime import datetime
from django.urls import reverse
from accounts.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class JobListing(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    salary_range = models.CharField(max_length=20)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", args=[self.id])

