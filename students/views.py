from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from students.forms import StudentCreateForm
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
    students = Student.objects.all()

    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    rating = request.GET.get('rating')

    if first_name:
        or_names = first_name.split('|')
        or_cond = Q()
        for or_name in or_names:
            or_cond = or_cond | Q(first_name=or_name)
        students = students.filter(or_cond)

    if last_name:
        students = students.filter(last_name=last_name)

    if rating:
        students = students.filter(rating=rating)

    return render(
        request=request,
        template_name='students-list.html',
        context={
            'students': students
        }

    )


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
            'form': form
        }
    )


def edit_student(request, pk):

    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponse("Student doesn't exist", status=404)

    if request.method == 'GET':

        form = StudentCreateForm(instance=student)

    elif request.method == 'POST':

        form = StudentCreateForm(
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
            'form': form
        }
    )
