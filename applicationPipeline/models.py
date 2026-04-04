from django.db import models
from accounts.models import User  
class Application(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("screening", "Screening"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]

    job = models.ForeignKey(
        "jobListings.JobListing",
        on_delete=models.CASCADE,
        related_name="applications"
    )
    
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications",
        null=True,    
        blank=True
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="applied")
    notes = models.TextField(blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        candidate_name = self.candidate.username if self.candidate else "Unknown"
        return f"{candidate_name} - {self.job.title}"