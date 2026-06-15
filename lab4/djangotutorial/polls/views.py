from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world, My Name is Marwan Ashraf. You're at the polls index.")
