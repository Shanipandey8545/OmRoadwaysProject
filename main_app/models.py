from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    ROLE_TYPE = [
        ('SuperAdmin','SuperAdmin'),
        ('Admin','Admin'),
        ('Driver','Driver'),
        ('Helper','Helper'),        
    ]
    
    role = models.CharField(max_length=50, choices=ROLE_TYPE, default='Admin')
    phone = models.CharField(max_length=15,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_image = models.FileField(upload_to='user_profile', null=True, blank=True)
    license_number = models.CharField(max_length=100, null=True, blank=True)
    aadhar_number = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Vehicle(models.Model):
    VEHICLE_TYPE = [
        ('Trailer','Trailer'),
        ('Truck','Truck'),
    ]

    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPE)
    capacity = models.CharField(max_length=50)  # like 20 Ton, 40 Ton
    driver = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='driver', null=True, blank=True)
    helper = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='helper', null=True, blank=True)
    insurance_number = models.CharField(max_length=100)
    fitness_expiry = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
  
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    logo = models.FileField(upload_to='company_logo', null=True, blank=True)  
    
# class Shipment(models.Model):
#     STATUS_TYPE = [
#         ('Pending','Pending'),
#         ('In Transit','In Transit'),
#         ('Delivered','Delivered'),
#     ]

#     load_id = models.CharField(max_length=100)
#     material = models.CharField(max_length=200)
#     from_location = models.CharField(max_length=200)
#     to_location = models.CharField(max_length=200)
#     weight = models.CharField(max_length=50)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     driver = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, choices=STATUS_TYPE, default='Pending')
#     dispatch_date = models.DateField()
#     delivery_date = models.DateField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
# class Payment(models.Model):
#     PAYMENT_STATUS = [
#         ('Pending','Pending'),
#         ('Paid','Paid'),
#     ]

#     shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
#     payment_date = models.DateField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
