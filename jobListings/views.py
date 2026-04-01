from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import JobListing  

def index(request):
    job_list = JobListing.objects.all()
    return render(request, "jobListings/index.html", {"job_list": job_list})

def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, "jobListings/job_detail.html", {"job": job})