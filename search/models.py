from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255) 
    company = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)   
    location = models.CharField(max_length=100)
    seniority = models.CharField(max_length=50) 
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.company}"