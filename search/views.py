from django.shortcuts import render
from jobListings.models import JobListing
from django.db.models import Q

def search_view(request):
    keyword = request.GET.get("keyword", "").strip()
    location = request.GET.get("location", "").strip()
    level = request.GET.get("level", "").strip()

    results = JobListing.objects.all()

    if keyword:
        results = results.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword) |
            Q(company__name__icontains=keyword)
        )

    if location:
        results = results.filter(location__icontains=location)

    if level and level != "all":
        results = results.filter(level__iexact=level)

    return render(request, "search/search.html", {"results": results})
