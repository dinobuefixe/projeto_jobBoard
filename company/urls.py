from django.urls import path
from .views import edit_company_view

urlpatterns = [
    path("edit/", edit_company_view, name="edit_company"),
]
