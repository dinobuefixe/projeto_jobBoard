from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Application
from jobListings.models import JobListing
from .forms import ApplicationStatusForm

def applications_list(request):
    if request.user.is_authenticated:
        applications = Application.objects.filter(candidate=request.user)
    else:
        applications = Application.objects.none()

    search_query = request.GET.get("search")
    if search_query:
        applications = applications.filter(
            Q(job__title__icontains=search_query) |
            Q(job__company__name__icontains=search_query)
        )

    status_filter = request.GET.get("status")
    if status_filter:
        applications = applications.filter(status=status_filter)

    sort = request.GET.get("sort")
    if sort == "newest":
        applications = applications.order_by("-created_at")
    elif sort == "oldest":
        applications = applications.order_by("created_at")

    context = {
        "applications": applications,
        "search_query": search_query,
        "status_filter": status_filter,
        "sort": sort,
    }
    return render(request, 'applicationPipeline/application_list.html', context)

@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)

    already_applied = Application.objects.filter(job=job, candidate=request.user).exists()

    if not already_applied:
        Application.objects.create(
            job=job,
            candidate=request.user,
            status="applied"
        )

    return redirect("application_list")


def update_status_view(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    return render(request, 'applicationPipeline/update_status.html', {'application': application})


@login_required
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    # Só o candidato pode apagar a candidatura
    if application.candidate != request.user:
        return redirect("account", pk=request.user.pk)

    application.delete()
    return redirect("account", pk=request.user.pk)

@login_required
def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    # Só o candidato pode editar
    if application.candidate != request.user:
        return redirect("account", pk=request.user.pk)

    if request.method == "POST":
        form = ApplicationEditForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = ApplicationEditForm(instance=application)

    return render(request, "applicationPipeline/edit_application.html", {"form": form})

@login_required
def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    # Apenas o employee dono da candidatura pode editar
    if application.candidate != request.user:
        return redirect("account", pk=request.user.pk)

    if request.method == "POST":
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = ApplicationStatusForm(instance=application)

    return render(request, "applicationPipeline/edit_application.html", {"form": form})

@login_required
def employer_edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    # Só o EMPLOYER dono da vaga pode editar
    if not request.user.is_employer:
        return redirect("home")

    if application.job.company != request.user.company:
        return redirect("home")

    if request.method == "POST":
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = ApplicationStatusForm(instance=application)

    return render(request, "applicationPipeline/employer_edit_application.html", {"form": form, "application": application})
