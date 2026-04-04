from django.urls import path
from .views import create_job_view, index, job_detail

urlpatterns = [
    path("", index, name="index"),
    path("job/<int:pk>/", job_detail, name="job_detail"),
    path("create/", create_job_view, name="create_job"),
]
