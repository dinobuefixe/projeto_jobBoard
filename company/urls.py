from django.urls import path
from .views import edit_company

urlpatterns = [
    path('company/edit/', edit_company, name='edit_company'),]
