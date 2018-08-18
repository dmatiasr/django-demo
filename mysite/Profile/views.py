from django.shortcuts import render
from .models import Professional


def index(request):
    return render(request, 'dashboard/profile_dashboard_section.html', {})


def get_proffesionals(request):
    '''
    Funcion que retorna todos los Profesionales de la base de datos.
    :param request:
    :return: Queryset Professionals
    '''

    try:
        return render(
            request,
            'dashboard/profile/profile_professionals_section.html',
            {'professionals': Professional.objects.all()}
        )
    except Professional.DoesNotExist:
        return render(
            request,
            'dashboard/profile_dashboard_section.html'
        )
