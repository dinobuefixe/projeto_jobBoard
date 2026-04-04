from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import JobListing
from .forms import JobForm
from django.contrib.auth.decorators import login_required

def index(request):
    job_list = JobListing.objects.all()
    return render(request, "jobListings/index.html", {"job_list": job_list})


def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, "jobListings/job_detail.html", {"job": job})


@login_required
def create_job_view(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = JobForm()

    return render(request, "jobs/create_job.html", {"form": form})

def home(request):
    recent_jobs = JobListing.objects.order_by('-date_published')[:5]
    return render(request, 'jobListings/home.html', {'recent_jobs': recent_jobs})