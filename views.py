from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Attendance


def home(request):
    return render(request, 'home.html')


def get_students(request):
    students = Student.objects.all()

    search = request.GET.get('search')

    if search:
        students = students.filter(name__icontains=search)

    data = []

    for student in students:
        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            present=True
        ).count()

        if total > 0:
            percentage = round((present / total) * 100, 2)
        else:
            percentage = 0

        data.append({
            'id': student.id,
            'name': student.name,
            'roll_no': student.roll_no,
            'course': student.course,
            'email': student.email,
            'attendance': percentage
        })

    return JsonResponse(data, safe=False)
