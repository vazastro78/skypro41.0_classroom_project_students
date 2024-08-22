from django.shortcuts import render

from students.models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()

    context = {
        'student_list': students
    }

    return render(request, 'students/mainpage.html', context)
