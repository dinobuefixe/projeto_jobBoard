from django.urls import path
from .views import applications_list

urlpatterns = [
    path('', applications_list, name='application-list'),
]