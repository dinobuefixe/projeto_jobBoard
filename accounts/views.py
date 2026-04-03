from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from accounts.models import User

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
    user = get_object_or_404(User, pk=pk)

    if request.user.pk != user.pk:
        return redirect("home")

    return render(request, "accounts/account.html", {"user": user})

@login_required
def create_job_view(request):
    return render(request, "jobs/create_job.html")


@login_required
def edit_company_view(request):
    return render(request, "company/edit_company.html")

