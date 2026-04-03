from django.urls import path
from .views import signup_view, login_view, account_view, create_job_view, edit_company_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("account/<int:pk>/", account_view, name="account"),
    path("create/", create_job_view, name="create_job"),
    path("company/edit/", edit_company_view, name="edit_company"),
    path("edit/", edit_company_view, name="edit_company"),
]