"""
URL configuration for compliance_project project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("compliance_checker.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("terms/", TemplateView.as_view(template_name="terms.html"), name="terms"),
    path("privacy/", TemplateView.as_view(template_name="privacy.html"), name="privacy"),
]
