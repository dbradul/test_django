from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from students.utils import parse_length, gen_password


def hello(request):
    return HttpResponse('Hello from Django!')


def get_random(request):
    try:
        length = parse_length(request, 10)
    except Exception as ex:
        return HttpResponse(str(ex), status_code=400)

    result = gen_password(length)

    return HttpResponse(result)
