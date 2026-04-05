from django.urls import path
from .views import apply_to_job_view, index, job_detail, create_job_view

urlpatterns = [
    path("", index, name="home"),
    path("job/<int:pk>/", job_detail, name="job_detail"),
    path("create/", create_job_view, name="create_job"),
    path("job/<int:pk>/apply/", apply_to_job_view, name="apply_to_job"),
]
