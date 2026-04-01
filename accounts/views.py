from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup') 
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    from django.contrib.auth import login
    from django.shortcuts import redirect, render
    from .forms import LoginForm

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        if user.is_employee:
            return redirect("employee_dashboard")
        elif user.is_employer:
            return redirect("employer_dashboard")

        return redirect("home")

    return render(request, "accounts/login.html", {"form": form})