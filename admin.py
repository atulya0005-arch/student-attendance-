from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'course', 'email')
    search_fields = ('name', 'roll_no')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present')
    list_filter = ('date', 'present')
