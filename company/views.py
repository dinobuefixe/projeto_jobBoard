from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

@login_required
def edit_company(request):
    # tenta obter a empresa do utilizador, ou None
    company = getattr(request.user, 'company', None)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect('edit_company')  # ou outra página, se quiseres
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'company/edit_company.html', context)
