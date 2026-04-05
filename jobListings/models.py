from django.db import models
from datetime import datetime
from django.urls import reverse
from company.models import Company  # use the real Company model
from django.conf import settings


class JobListing(models.Model):
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    salary_range = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", args=[self.id])
