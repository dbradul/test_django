from django.urls import path

from students.views import create_student, edit_student, get_students

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('edit/<int:pk>', edit_student, name='edit'),
]
