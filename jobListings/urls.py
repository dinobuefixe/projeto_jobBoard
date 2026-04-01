from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("job/<int:pk>/", views.job_detail, name="job_detail"),
]
