from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobListing
from .forms import JobListingForm
from company.models import Company
from applicationPipeline.services.applications_service import create_application
from applicationPipeline.models import Application

def job_list_view(request):
    jobs = JobListing.objects.all().order_by("-date_published")
    return render(request, "jobListings/index.html", {"jobs": jobs})


def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, "jobListings/job_detail.html", {"job": job})

@login_required
def apply_to_job(request, pk):
    job = get_object_or_404(JobListing, pk=pk)

    # Só employees podem candidatar-se
    if not request.user.is_employee:
        return redirect("job_detail", pk=pk)

    # Evitar candidaturas duplicadas
    existing = Application.objects.filter(job=job, candidate=request.user).first()
    if existing:
        return redirect("job_detail", pk=pk)

    # Criar candidatura
    Application.objects.create(
        job=job,
        candidate=request.user,
        status="applied"
    )

    return redirect("account", pk=request.user.pk)

@login_required
def create_job_view(request):
    # Apenas empregadores podem criar vagas
    if not request.user.is_employer:
        return redirect("home")

    # Empregador precisa de ter empresa criada
    if not hasattr(request.user, "company"):
        return redirect("edit_company")

    if request.method == "POST":
        form = JobListingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()

            # NÃO criamos Application aqui — só quando um candidato se candidata

            return redirect("account", pk=request.user.pk)

    else:
        form = JobListingForm()

    return render(request, "jobListings/create_job.html", {"form": form})

