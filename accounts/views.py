from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from applicationPipeline.models import Application  
from jobListings.models import JobListing

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    from django.contrib.auth import login

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("account", pk=user.pk)

    return render(request, "accounts/login.html", {"form": form})

@login_required
def account_view(request, pk):
    user = request.user

    jobs = None
    received_applications = None
    sent_applications = None

    # EMPLOYER
    if user.is_employer:
        # vagas da empresa
        jobs = JobListing.objects.filter(company=user.company)

        # candidaturas recebidas
        received_applications = Application.objects.filter(job__company=user.company)

    # EMPLOYEE
    if user.is_employee:
        # candidaturas enviadas
        sent_applications = Application.objects.filter(candidate=user)

    context = {
        "user": user,
        "jobs": jobs,
        "applications": received_applications,   # para employer
        "sent_applications": sent_applications,  # para employee
    }

    return render(request, "accounts/account.html", context)
