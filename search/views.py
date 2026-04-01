from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q
from jobListings.models import JobListing

def search_view(request):
    results = JobListing.objects.all()

    keyword = request.GET.get('keyword')
    location = request.GET.get('location')
    level = request.GET.get('level')

    if keyword:
        results = results.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword)
        )

    if location:
        results = results.filter(location__icontains=location)

    if level:
        results = results.filter(level__iexact=level)

    return render(request, "search/search.html", {"results": results})