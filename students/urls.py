from django.urls import path

from students.views import (
    create_student,
    edit_student,
    get_students,
    delete_student
)

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('edit/<uuid:uuid>', edit_student, name='edit'),
    path('delete/<uuid:uuid>', delete_student, name='delete'),
]
