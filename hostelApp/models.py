from datetime import datetime
from pyexpat import model
from tokenize import Name
from django.db import models

# Create your models here.

class Admins(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField()
  password=models.IntegerField()
  phone_number=models.CharField(max_length=10)


class Room_details(models.Model):
  room_Name=models.CharField(max_length=25)
  room_Location=models.CharField(max_length=50)
  number_Of_Beds=models.IntegerField()
  numberOfStudents=models.IntegerField()
  status=models.BooleanField() 
CHOICES=(
         ("M","occupied"),
      ("F","Not occupied"),
 )

room_Number=models.IntegerField()
 
class Student_Registration(models.Model):
  stud_Name=models.CharField(max_length=25)
  dob=models.DateTimeField(default=datetime.now)
  GENDER_CHOICES=(
        ("M","MALE"),
        ("F","FEMALE"),
    )
  gender=models.BooleanField()
    
  status=models.BooleanField()
  admission_Date=models.DateTimeField()
  phonenumber=models.CharField(max_length=10)
  studentAdmissionNumber=models.CharField(max_length=10)
  id_number=models.CharField(max_length=15)
  parent_Name=models.CharField(max_length=20)
  parent_Contact=models.CharField(max_length=10)



class Guardian_Detail(models.Model):
  name=models.CharField(max_length=20)
  id_number=models.CharField(max_length=20)
  email_address=models.EmailField()
  address=models.CharField(max_length=15)
  phonenumber=models.CharField(max_length=15)
  admission_date=models.DateTimeField(default=datetime.now)

class Receipt(models.Model):
   stud_Name=models.ForeignKey("Receipt",on_delete=models.CASCADE,related_name='Student_Registration_Receipt')
   studentAdmissionNumber=models.ForeignKey("Receipt",on_delete=models.CASCADE,related_name='StudAdmissionNumber_Receipt')
   amount=models.IntegerField()
   course=models.CharField(max_length=20)
   signature=models.ImageField()
   dateOfPayment=models.DateTimeField(default=datetime.now)

class Clearance(models.Model):
   name=models.CharField(max_length=20)
   admissionNumber=models.CharField(max_length=15)
   email_address=models.EmailField()
   completion_date=models.DateTimeField(default=datetime.now)
   phonenumber=models.CharField(max_length=10)
   admission_Date=models.DateTimeField(default=datetime.now)

class Notification(models.Model):
   name=models.CharField(max_length=20)
   studentId=models.CharField(max_length=15)
   email_address=models.EmailField()
   description=models.CharField(max_length=50)
   institution=models.CharField(max_length=20)
   notification_Origin=models.CharField(max_length=15)
   notification_Destination=models.CharField(max_length=15)
   dateOfnotification=models.DateTimeField(default=datetime.now)














