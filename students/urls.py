from django.urls import path

from students.views import create_student, get_students, edit_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('edit/<int:id>', edit_student, name='edit'),
]
