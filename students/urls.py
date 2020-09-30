from django.urls import path

from students.views import (
    delete_student, StudentUpdateView, StudentCreateView, StudentListView
)

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('edit/<uuid:uuid>', StudentUpdateView.as_view(), name='edit'),
    path('delete/<uuid:uuid>', delete_student, name='delete'),
]
