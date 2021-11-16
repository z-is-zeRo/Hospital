from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Departments, Doctors, Patients, Appointments, Payments
import random as r

# Create your views here.
def home(request):
    patients = Patients.objects.all().count()
    return render(request, 'management/index.html',{'patients':patients})

def doctors(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request, 'management/doctors.html', context)

def department_doctors(request, name):
    department  = Departments.objects.get(name=name)
    doctors = Doctors.objects.filter(department=department)
    context = {
        'doctors': doctors,
    }
    return render(request, 'management/department-doctors.html', context)
    

def doctors_profile(request, pk):
    doctor = Doctors.objects.get(pk=pk)
    return render(request, 'management/profile.html', {'doctor': doctor})

def add_doctors(request):
    return render(request, 'management/add-doctor.html')

def patients(request):
    patients = Patients.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'management/patients.html', context)

def patients_profile(request, pk):
    patient = Patients.objects.get(pk=pk)
    return render(request, 'management/patient-profile.html', {'patient':patient})

def add_patients(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        speciality = request.POST.get('speciality')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        
        id_number = r.randint(9999, 1000000)
        
        Patients.objects.create(
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            gender = gender,
            phone = phone,
            email = email,
            description = description,
            occupation = speciality,
            id_number = 'POLYCLINIC' + str(id_number)
        )
        
        messages.info(request, 'Your id number is:' + 'POLYCLINIC' + str(id_number))
        return redirect('management:patients')
    
    return render(request, 'management/add-patient.html')

def payments(request):
    payments = Payments.objects.all()
    return render(request, 'management/payments.html', {'payments': payments})

def add_payments(request):
    if request.method == 'POST':
        payment_number = request.POST.get('payment_number')
        patient_name = request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        payment_date = request.POST.get('payment_date')
        amount = request.POST.get('amount')
        payment_method= request.POST.get('payment_method')
        payment_status = request.POST.get('payment_status')
        
        Payments.objects.create(
            payment_number = payment_number,
            patient = patient_name,
            doctor = doctor_name,
            date = payment_date,
            amount = amount,
            payment_method = payment_method,
            payemtn_status = payment_status,
        )
        
        messages.info(request, 'Your payment has been received')
        return redirect("management:payments")
        
    return render(request, 'management/add-payments.html')

def schedule(request):
    appointments = Appointments.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request,'management/doctor-schedule.html', context )

def departments(request):
    departments = Departments.objects.all()
    context = {
        'departments': departments
    }
    return render(request,'management/departments.html', context )

def appointment(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        service = request.POST.get('service')
        date = request.POST.get('date')
        email = request.POST.get('email')

        Appointments.objects.create(
            first_name = first_name,
            last_name = last_name,
            department = service,
            date_issued = date,
            email = email,
        )
        
        messages.info(request, 'Your appointment has been made')
        return redirect('management:schedule')
    
    return render(request,'management/book-appointment.html' )


def search(request):
    if request.method == 'POST':
        results = request.POST.get('search')
        patients = Patients.objects.filter(first_name__icontains = results)
        if patients is None:
            patients = Patients.objects.filter(last_name__icontains = results)
        context = {
            'patients':patients
        }
    return render(request, 'management/search_results.html',context)