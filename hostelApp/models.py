from datetime import datetime
from pyexpat import model
from tokenize import Name
from django.db import models

# Create your models here.

class Admin(models.Model):
    Name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.IntegerField()
    phone_number=models.CharField(max_length=10)


class Room(models.Model):
 Room_Name=models.CharField(max_length=25)
 room_Location=models.CharField()
 Number_Of_Beds=models.IntegerField()
 NumberOfStudents=models.IntegerField()
 status=models.BooleanField() 
 Room_Number=models.IntegerField()
 
class Student_Registration(models.Model):
    Stud_Name=models.CharField(max_length=25)
    DOB=models.DateTimeField(default=datetime.now)
    GENDER_CHOICES=(
        ("M","MALE"),
        ("F","FEMALE"),
    )
    Gender=models.BooleanField()
    
    status=models.BooleanField()
    admission_Date=models.DateTimeField()
    phonenumber=models.CharField()
    studentAdmissionNumber=models.CharField()
    Id_number=models.CharField()
    Parent_Name=models.CharField(max_length=20)
    Parent_Contact=models.CharField()



class Guardian_Details(models.Models):
        Name=models.CharField(max_length=20)
        id_number=models.CharField()
        Email_address=models.EmailField()
        address=models.CharField()
        phonenumber=models.CharField(max_length=15)
        admission_date=models.DateTimeField(default=datetime.now)

class Receipt(models.Model):
         Stud_Name=models("Receipt",on_delete=models.CASCADE,related_name='Student_Registration_Receipt')
         studentAdmissionNumber=models("Receipt",on_delete=models.CASCADE,related_name='StudAdmissionNumber_Receipt')
         amount=models.IntegerField()
         course=models.CharField()
         signature=models.ImageField()
         dateOfPayment=models.DateTimeField(default=datetime.now)

class clearance (models.Model):
            Name=models("Clearance",on_delete=models.CASCADE,related_name='Student_Registration_Clearance')
            AdmissionNumber=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
            Email_address=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
            Completion_date=models.DateTimeField(default=datetime.now)
            phonenumber=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
            admission_Date=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')

class Notification(models.Models):
                Name=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
                studentId=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
                Email_address=models("Clearance",on_delete=models.CASCADE,related_name='Stud_Registration_Clearance')
                description=models.CharField()
                institution=models.CharField()
                Notification_Origin=models.CharField
                Notification_Destination=models.CharField()
                DateOfnotification=models.DateTimeField(default=datetime.now)














