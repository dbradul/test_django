from django.contrib import admin

# Register your models here.
from groups.models import Classroom, Group
from students.models import Student

class StudentTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name', 'email']
    readonly_fields = fields
    show_change_link = True
    list_per_page = 10

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'head']
    fields = ['name', 'course', 'head', 'classrooms']
    inlines = [StudentTable]
    list_select_related = ['head']
    list_per_page = 2

admin.site.register(Classroom)
admin.site.register(Group, GroupAdmin)