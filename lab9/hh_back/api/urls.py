from django.urls import path
from . views import *

urlpatterns = [
    path('companies/', company_list , name='company_list'),
    path('companies/<int:id>/', get_company , name='get_company'),
    path('companies/<int:id>/vacancies', company_vacancies, name='company_vacancies'),
    path('vacancies/', vacancy_list, name='vacancy_list'),
    path('vacancies/<int:id>/', get_vacancy, name='get_vacancy'),
    path('vacancies/top_ten/', top_ten_vacancies , name='top_ten_vacancies'),
]