from django.urls import path
from .views import edit_application, delete_application, applications_list, apply_to_job, employer_edit_application

urlpatterns = [
    path('', applications_list, name='application_list'),
    path('apply/<int:job_id>/', apply_to_job, name='apply_to_job'), 
    path("edit/<int:pk>/", edit_application, name="edit_application"),    
    path("delete/<int:pk>/", delete_application, name="delete_application"),
    path("employer/edit/<int:pk>/", employer_edit_application, name="employer_edit_application"),
]