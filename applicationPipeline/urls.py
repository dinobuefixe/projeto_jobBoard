from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications_list, name='application_list'),
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'), # New path
]