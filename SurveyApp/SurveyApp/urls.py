"""SurveyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls, name="admin"),
    re_path(r'^$', views.homepage, name="homepage"),
    re_path(r'^consent/', views.consent, name="consent"),
    re_path(r'^survey/', views.survey, name="survey"),
    re_path(r'^thank-you/', views.dashboard, name="dashboard"),
    re_path(r'delete/', views.delete_my_data, name="delete-my-data"),
]
