from django.shortcuts import render
from .models import Job
from django.db.models import Q 

def search_view(request):
    results = Job.objects.all()

    keyword = request.GET.get('keyword')
    stack = request.GET.get('stack')
    location = request.GET.get('location')
    seniority = request.GET.get('seniority')

    if keyword:
        results = results.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
    if stack:
        results = results.filter(stack__icontains=stack)
    if location:
        results = results.filter(location__icontains=location)
    if seniority:
        results = results.filter(seniority__iexact=seniority)

    return render(request, 'search/search.html', {'results': results})