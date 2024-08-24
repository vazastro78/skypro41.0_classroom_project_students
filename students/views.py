from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from students.models import Student

# Create your views here.

#CBV
class StudentListView(ListView):
    model = Student
    template_name = 'students/mainpage.html'

#CBV
class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'


