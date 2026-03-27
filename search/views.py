from django.shortcuts import render
from .models import JobListing
from django.db.models import Q 
from django.utils import timezone

def search_view(request):
    from django.shortcuts import render
    from django.db.models import Q
    from jobListings.models import JobListing  
    from django.utils import timezone

def search_view(request):
    results = JobListing.objects.all()

    keyword = request.GET.get('keyword')
    stack = request.GET.get('stack')
    location = request.GET.get('location')
    seniority = request.GET.get('seniority')

    if keyword:
        results = results.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword) 
        )

    if stack:
        results = results.filter(stack__icontains=stack)

    if location:
        results = results.filter(location__icontains=location)

    if seniority:
        results = results.filter(level__iexact=seniority)  

    return render(request, 'search/search.html', {'results': results})