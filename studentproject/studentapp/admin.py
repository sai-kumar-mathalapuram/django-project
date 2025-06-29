from django.contrib import admin
from studentapp.models import studentinfo
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['roll_number','fullname', 'date_of_birth','email']
admin.site.register(studentinfo,StudentAdmin)