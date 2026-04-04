from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

@login_required
def edit_company_view(request):
    company, created = Company.objects.get_or_create(owner=request.user)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("account", pk=request.user.pk)
    else:
        form = CompanyForm(instance=company)

    return render(request, "company/edit_company.html", {"form": form})
