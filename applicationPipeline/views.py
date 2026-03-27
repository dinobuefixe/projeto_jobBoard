from django.shortcuts import render
from django.db.models import Q
from .models import Application


def applications_list(request):
    applications = Application.objects.all()

    search_query = request.GET.get("search")
    if search_query:
        applications = applications.filter(
            Q(job_title__icontains=search_query) |
            Q(company__icontains=search_query)
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


def update_status_view(request, app_id):
    return render(request, 'applicationPipeline/update_status.html')