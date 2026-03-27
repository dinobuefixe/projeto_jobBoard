from django.db import models
from accounts.models import User
from jobListings.models import JobListing

class Application(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("screening", "Screening"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]

    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="applied")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"
