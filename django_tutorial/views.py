from django.http import HttpResponse
from django.shortcuts import render # Used to return HTML


def hello(request):
    return render(request, 'home.html')
