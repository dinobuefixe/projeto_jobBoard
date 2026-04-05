from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobListing
from .forms import JobForm
from company.models import Company
from applicationPipeline.services.applications_service import create_application

def index(request):
    job_list = JobListing.objects.all()
    return render(request, "jobListings/index.html", {"job_list": job_list})

def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, "jobListings/job_detail.html", {"job": job})

@login_required
def apply_to_job_view(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    company = job.company

    if request.method == "POST":
        message = request.POST.get("message", "")
        create_application(request.user, job, company, message)
        return redirect("job_detail", pk=job.pk)

    return render(request, "jobListings/apply.html", {"job": job})

@login_required
def create_job_view(request):
    if not request.user.is_employer:
        return redirect("account", pk=request.user.pk)

    company = Company.objects.get(owner=request.user)

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = JobForm()

    return render(request, "jobListings/create_job.html", {"form": form})