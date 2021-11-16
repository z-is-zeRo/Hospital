from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.name}"
    
class Doctors(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 200)
    date_of_birth = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    location = models.CharField(max_length = 230)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:doctors_profile', kwargs={
            'pk': self.pk
        })
    
class Registration(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    duty = models.CharField(max_length = 200)
    ward_no = models.CharField(max_length = 200)
    date = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.doctor} - {self.duty}"
    
class Patients(models.Model):
    first_name = models.CharField(max_length = 200, null = True, blank = True)
    last_name = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 200, null = True, blank = True)
    gender = models.CharField(max_length = 200, null = True, blank = True)
    date_of_birth = models.CharField(max_length = 200, null = True, blank = True)
    email = models.CharField(max_length = 200, null = True, blank = True)
    location = models.CharField(max_length = 230, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    profile = models.ImageField(null = True, blank = True)
    occupation = models.CharField(max_length = 200, null = True, blank = True)
    biography = models.TextField(null = True, blank = True)
    timeline = models.TextField(null = True, blank = True)
    bloodpressure = models.CharField(max_length = 200, null = True, blank = True)
    heartbeat = models.CharField(max_length = 200, null = True, blank = True)
    haemoglobin = models.CharField(max_length = 200, null = True, blank = True)
    sugar = models.CharField(max_length = 200, null = True, blank = True)
    education = models.TextField(null = True, blank = True)
    history = models.TextField(null = True, blank = True)
    id_number = models.CharField(max_length = 200, null = True, blank = True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('management:patients_profile', kwargs={
            'pk': self.pk
        })
    
class Appointments(models.Model):
    first_name = models.CharField(max_length = 200, null = True, blank = True)
    last_name = models.CharField(max_length = 200,  null = True, blank = True)
    gender = models.CharField(max_length = 200,  null = True, blank = True)
    phone= models.CharField(max_length = 200,  null = True, blank = True)
    date_of_birth = models.CharField(max_length = 200,  null = True, blank = True)
    email = models.CharField(max_length = 200,  null = True, blank = True)
    date_issued = models.CharField(max_length = 200, null = True, blank = True)
    department = models.CharField(max_length = 200, null = True, blank = True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class DoctorsSchedule(models.Model):
    date = models.DateField()
    event = models.TextField()
    
    def __str__(self):
        return f"{self.event} {self.date}"
    
    
class Payments(models.Model):
    payment_number = models.CharField(max_length = 200)
    patient = models.CharField(max_length = 200)
    doctor = models.CharField(max_length = 200)
    date = models.CharField(max_length = 200)
    amount = models.CharField(max_length = 200)
    payment_method = models.CharField(max_length = 200)
    payemtn_status = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.payment_number} {self.patient}"
    