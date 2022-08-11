from django.contrib import admin
# Register your models here.
# from tkinter import N

from .models import Admin,StudentDetails,Classroom,RoomAllotment,StudentRegistration,StudentsGuardian,Receipt,RoomFees,ClearanceForm,ClearanceMessage,Notification
 

class Admin(admin.ModelAdmin):
    list_display=("first_name","last_name","age","email")
    search_fields=("first_name","last_name")

admin.site.register(Admin)
admin.site.register(StudentDetails)
admin.site.register(Classroom)
admin.site.register(RoomAllotment)
admin.site.register(StudentRegistration)
admin.site.registe(Receipt)
admin.site.register(RoomFees)
admin.site.register(ClearanceForm)
admin.site.register(ClearanceMessage)
admin.site.register(Notification)