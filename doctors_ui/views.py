from django.shortcuts import render, redirect
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

    return render(request, 'doctor-detail.html', {'doctor': doctor})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        response = requests.post('http://localhost:8000/login/', data={"username":username, "password":password})
        if response.status_code == 200:
            request.session['token'] = response.json().get('token')
            return redirect('deparment-list')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def api_request_with_token(request, url, method='get', data=None):
    token = request.session['auth_token']
    headers = {}
    if token:
        headers['authorization'] = f'Token {token}'
    if method == 'get':
        resp = requests.get(url, headers)
    elif method == 'post':
        resp = requests.post(url, json=data, headers=headers)
    return resp

def logout_view(request):
    if 'auth_token' in request.session:
        del request.session['auth_token']
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }

        try:
            response = requests.post(
                'http://localhost:8000/register/', 
                json=data  # <-- use json= not data= here 
            )
        except requests.exceptions.RequestException:
            return render(request, 'registration/register.html', {'errors': {'error': 'API request failed'}})

        if response.status_code == 201:
            try:
                token = response.json().get('token')
                if token:
                    request.session['auth_token'] = token
            except ValueError:
                # handle JSON decode error gracefully
                return render(request, 'registration/register.html', {'errors': {'error': 'Invalid API response'}})
            return redirect('login')

        else:
            try:
                errors = response.json()
            except ValueError:
                errors = {'error': 'Invalid API error response'}
            return render(request, 'registration/register.html', {'errors': errors})

    return render(request, 'registration/register.html')

def profile_view(request):
    api_url = 'http://localhost:8000/profile/'
    response = api_request_with_token(request, api_url)
    if response.status_code == 200:
        profile = response.json()
        return render(request, 'registration/profile.html', {'profile':profile})
    else:
        return redirect('login')
    
