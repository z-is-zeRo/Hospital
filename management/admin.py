from django.contrib import admin
from .models import Departments, Doctors, Patients, Appointments, Registration, DoctorsSchedule, Payments
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department']
    search_fields = ('first_name', 'last_name', 'department' )
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'description']
    search_fields = ('first_name', 'last_name' )
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_issued']
    search_fields = ('first_name', 'last_name' )
    
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['payment_number', 'patient', 'amount', 'payemtn_status']
    search_fields = ('payment_number', 'patient', 'payemtn_status' )

admin.site.register(Departments)
admin.site.register(Doctors, DoctorAdmin)
admin.site.register(Patients, PatientAdmin)
admin.site.register(Appointments, AppointmentAdmin)
admin.site.register(Registration)
admin.site.register(DoctorsSchedule)
admin.site.register(Payments, PaymentsAdmin)

