from django.urls import path
from .views import apply_to_job, job_detail, create_job_view, job_list_view

urlpatterns = [
    path("", job_list_view, name="job_list"),
    path("job/<int:pk>/", job_detail, name="job_detail"),
    path("create/", create_job_view, name="create_job"),
    path("job/<int:pk>/apply/", apply_to_job, name="apply_to_job"),
]
