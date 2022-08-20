from unicodedata import name
from django.contrib import admin
# Register your models here.
# from tkinter import N

from .models import Admins, Room_details,Student_Registration,Guardian_Detail,Receipt,Notification,Clearance
 

class AdminstrationAdmin(admin.ModelAdmin):
    list_display=("name","password","email")
    search_fields=("email","name")
    admin.site.register(Admins)

class Room_detailsAdmin(admin.ModelAdmin):
     list_display=("room-Name","room_Location","number_of_beds","numberOfStudents","status","room_Number")
     search_fields=("room-Name","room_Location","number_of_beds","numberOfStudents","status","room_Number")
     admin.register(Room_details)

class Student_RegistrationAdmin(admin.ModelAdmin):
     list_display=("student_Name","dob","gender","status","admission_Date","phonenumber",'id_number',"parent_Name","parent_contact")
     search_fields=("student_Name","dob","gender","status","admission_Date","phonenumber",'id_number',"parent_Name","parent_contact")
     admin.register(Student_Registration)

class Guardian_DetailAdmin(admin.ModelAdmin):
    list_display=("name","id_number","email_address","address","phone","admission_date")
    search_fields=("name","id_number","email_address","address","phone","admission_date")
    admin.register(Guardian_Detail)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("stud_Name","student_Admission_Number","amount","course","signature","dateOfPayment")
    search_fields=("stud_Name","student_Admission_Number","amount","course","signature","dateOfPayment")
    admin.register(Receipt)

class NotificationAdmin(admin.ModelAdmin):
     list_display=("name","studentId","email_address","description","institution","notification_Origin", "notification_Destination","dateOfnotification")
     search_fields=("name","studentId","email_address","description","institution","notification_Origin", "notification_Destination","dateOfnotification")
     admin.register(Notification)
class ClearanceAdmin(admin.ModelAdmin):
    list_display=("name","admission_Number","email_address","completion_date","phonenumber","admission_date")
    search_fields=("name","admission_Number","email_address","completion_date","phonenumber","admission_date")
    admin.register(Clearance)


