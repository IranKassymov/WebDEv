"""
URL configuration for hh_back project.

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
from api.views import *


urlpatterns = [
    path('api/companies/', company_list , name='company_list'),
    path('api/companies/<int:id>/', get_company , name='get_company'),
    path('api/companies/<int:id>/vacancies', company_vacancies, name='company_vacancies'),
    path('api/vacancies/', vacancy_list, name='vacancy_list'),
    path('api/vacancies/<int:id>/', get_vacancy, name='get_vacancy'),
    path('api/vacancies/top_ten/', top_ten_vacancies , name='top_ten_vacancies'),
    path('admin/', admin.site.urls),
]
