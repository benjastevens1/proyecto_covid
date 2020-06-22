from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def registro(request):
    sintomass = {'habituales': ['Fiebre', 'Tos seca', 'Cansancio'],
                  'menos' : ['Molestias y Dolores', 'Dolor de Garganta', 'Diarrea', 'Conjuntivitis', 'Dolores de cabeza', 'Pérdida del olfato o del gusto', 'Erupciones cutáneas o pérdida del color en extremidades', 'Insuficiencia Respiratorias'],
                  'graves' : ['Dificultad para respirar o sensación de falta de aire', 'Dolor o presión en el pecho', 'Incapacidad para hablar o moverse']}

    return render(request, 'registro.html', sintomass)

def estadistica(request):
    return render(request, 'estadistica.html')