from django.urls import path
from .views import department_list_view, doctor_list_view, department_detail_view, doctor_detail_view

urlpatterns = [
    path('', department_list_view, name='deparment-list'),
    path('doctors/', doctor_list_view, name='doctor-list'),
    path('depatments/<int:id>/', department_detail_view, name='department-detail'),
    path('doctors/<int:id>/', doctor_detail_view, name='doctor-detail'),
]
