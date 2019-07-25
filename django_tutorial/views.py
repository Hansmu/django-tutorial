from django.http import HttpResponse
from django.shortcuts import render # Used to return HTML


def home(request):
    return render(request, 'home.html')


def translate(request):
    translation_text = request.GET['translationText']
    return HttpResponse("On the translate page: " + translation_text)
