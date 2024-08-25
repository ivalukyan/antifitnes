"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from bot_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.index, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('standards/', views.standards, name='standards'),
    path('standards/<int:pk>', views.StandardsID.as_view(), name='standards_id'),
    path('standards/create/', views.standards_create, name='standards_create'),
    path('profile/', views.profile, name='profile'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/create', views.createstatistics, name='create_statistics'),
    path('statistics/<str:year_id>/<str:norm_id>', views.statisticsID, name='statistic_id'),
    path('statistics/<str:year_id>', views.statistics_standards, name='statistics_standards')
]
