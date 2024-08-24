from django.urls import path
from students.views import StudentListView, StudentDetailView

urlpatterns = [
    path("", StudentListView.as_view(), name='student_list'),
    path("student/<int:pk>/", StudentDetailView.as_view(), name='student_detail'),
]
