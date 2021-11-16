from django.urls import path, include
from .views import home, doctors, add_doctors, doctors_profile,patients,add_patients,patients_profile,payments,schedule,appointment,add_payments,departments,department_doctors,search

app_name = 'management'

urlpatterns = [
    path('', home , name="home"),
    path('doctors/', doctors, name="doctors"),
    path('doctors/profile/<int:pk>/', doctors_profile, name="doctors_profile"),
    path('doctors/add/', add_doctors, name="add_doctors"),
    path('patients/', patients, name="patients"),
    path('patients/add', add_patients, name="add_patients"),
    path('patients/profile/<int:pk>/', patients_profile, name="patients_profile"),
    path('payments/', payments , name="payments"),
    path('appointment/', appointment , name="appointment"),
    path('schedule/', schedule , name="schedule"),
    path('add_payments/', add_payments , name="add_payments"),
    path('departments/', departments, name="departments"),
    path('department/doctors/<name>/', department_doctors, name="department_doctors"),
    path('search/', search, name="search")
]