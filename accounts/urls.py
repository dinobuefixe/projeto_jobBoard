from django.urls import path
from .views import signup_view, login_view, create_application

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path("apply/", create_application, name="application_create"),]