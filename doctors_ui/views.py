from django.shortcuts import render
import requests

def department_list_view(request):
    api_url = 'http://localhost:8000/api/departments/'

    try:
        response = requests.get(api_url)
        departments = response.json()
    except requests.RequestException:
        departments = []

    return render(request, 'base.html', {'departments': departments})

def department_detail_view(request, id):
    dept_api_url = f'http://localhost:8000/api/departments/{id}/'
    doctors_api_url = f'http://localhost:8000/api/doctors/?specialization={id}'

    try:
        dept_response = requests.get(dept_api_url)
        dept_response.raise_for_status()
        department = dept_response.json()
    except requests.RequestException:
        department = None

    try:
        doctors_response = requests.get(doctors_api_url)
        doctors_response.raise_for_status()
        doctors = doctors_response.json()
    except requests.RequestException:
        doctors = []

    context = {
        'department': department,
        'doctors': doctors,
    }

    return render(request, 'department-detail.html', context)

def doctor_list_view(request):
    api_url = 'http://localhost:8000/api/doctors/'

    try:
        response = requests.get(api_url)
        doctors = response.json()
    except requests.RequestException:
        doctors = []

    return render(request, 'doctor_list.html', {'doctors': doctors})


def doctor_detail_view(request, id):
    api_url = f'http://localhost:8000/api/doctors/{id}/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        doctor = response.json()
    except requests.RequestException:
        doctor = None

    return render(request, 'doctor_detail.html', {'doctor': doctor})