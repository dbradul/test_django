from django.contrib import admin  # noqa

# Register your models here.
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
     exclude = ['uuid']

admin.site.register(Student, StudentAdmin)