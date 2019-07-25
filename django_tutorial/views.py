from django.http import HttpResponse
from django.shortcuts import render  # Used to return HTML


def projects_home(request):
    return render(request, 'projects-navigation.html')


def latin_home(request):
    return render(request, 'pig-latin/latin-home.html')


def translate(request):
    translation_text = request.GET['translationText']
    translated_text = ''

    for word in translation_text.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translated_word = word
        else:
            translated_word = word[1:]
            translated_word += word[0]
            translated_word += 'ay'

        translated_text += translated_word + ' '

    return render(request, 'pig-latin/translate.html', {
        'original': translation_text,
        'translation': translated_text
    })  # Dictionary that is sent to the front for using
