from django.urls import path
from .views import department_list_view, doctor_list_view, department_detail_view, doctor_detail_view
from . import views

urlpatterns = [
    path('', department_list_view, name='deparment-list'),
    path('doctors/', doctor_list_view, name='doctor-list'),
    path('depatments/<int:id>/', department_detail_view, name='department-detail'),
    path('doctors/<int:id>/', doctor_detail_view, name='doctor-detail'),
]

urlpatterns += [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
