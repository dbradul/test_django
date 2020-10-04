from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from core.views import EditView
from students.forms import StudentCreateForm, StudentEditForm
from students.models import Student
from students.utils import gen_password, parse_length


def hello(request):
    return HttpResponse('Hello from Django!')


def get_random(request):
    try:
        length = parse_length(request, 10)
    except Exception as ex:
        return HttpResponse(str(ex), status_code=400)

    result = gen_password(length)

    return HttpResponse(result)


def get_students(request):
    students = Student.objects.select_related('group').all()

    or_params = [
        'first_name',
        'last_name',
    ]

    and_params = [
        'age',
        'date_start_work',
    ]

    for param in and_params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})

    for param in or_params:
        value = request.GET.get(param)
        if value:
            values = value.split('|')
            or_cond = Q()
            for value in values:
                or_cond |= Q(**{param: value})
            students = students.filter(or_cond)

    return render(
        request=request,
        template_name='students-list.html',
        context={
            'students': students,
        }
    )


# @csrf_exempt
def create_student(request):

    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students-create.html',
        context={
            'form': form,
        }
    )


def edit_student(request, uuid):

    try:
        student = Student.objects.get(uuid=uuid)
    except Student.DoesNotExist:
        return HttpResponse("Student doesn't exist", status=404)

    if request.method == 'GET':

        form = StudentEditForm(instance=student)

    elif request.method == 'POST':

        form = StudentEditForm(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students-edit.html',
        context={
            'form': form,
            'student': student,
        }
    )


def delete_student(request, uuid):
    '''
    def delete_student(request, uuid):
        Student.objects.get(uuid=uuid).delete()
        return HttpResponseRedirect(reverse("students:list"))
    '''
    student = get_object_or_404(Student, uuid=uuid)
    student.delete()

    return HttpResponseRedirect(reverse('students:list'))


class StudentEditView(EditView):

    model = Student
    form = StudentEditForm
    template_name = 'students-edit.html'
    redirect_url = 'students:list'
    object_name = 'student'
    pk_arg = 'uuid'

    def get_object(self, id):
        return self.model.objects.get(uuid=id)


class StudentUpdateView(LoginRequiredMixin, UpdateView):

    model = Student
    form_class = StudentEditForm
    template_name = 'students-edit.html'
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'
    pk_url_kwarg = 'uuid'

    def get_object(self):
        uuid = self.kwargs.get('uuid')
        return self.get_queryset().get(uuid=uuid)


class StudentCreateView(CreateView):

    model = Student
    form_class = StudentCreateForm
    template_name = 'students-create.html'
    success_url = reverse_lazy('students:list')


class StudentListView(ListView):

    model = Student
    # form_class = StudentCreateForm
    template_name = 'students-list.html'
    context_object_name = 'students'
    # success_url = reverse_lazy('students:list')

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        # ....

        return qs