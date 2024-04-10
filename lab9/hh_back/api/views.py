from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = {'companies' : list(companies.values())}
    return JsonResponse(data)

def get_company(request, id):
    company = list(Company.objects.filter(id ==id).values())
    return JsonResponse(company, safe = False)

def company_vacancies(request, id):
    # company = list(Company.objects.filter(id == id).values())
    vacancies = list(Vacancy.objects.filter(company= id).values())
    return JsonResponse(vacancies, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies' : list(vacancies.values())}
    return JsonResponse(data)

def get_vacancy(request, id):
    vacancy = list(Vacancy.objects.filter(id ==id).values())
    return JsonResponse(vacancy, safe = False)

def top_ten_vacancies(request):
    topten  = list(Vacancy.objects.order_by('-salary')[:10].values())
    return JsonResponse(topten, safe=False)
# Create your views here.
