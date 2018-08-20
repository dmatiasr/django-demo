from django.shortcuts import render
from .models import Professional


def index(request):
    return render(request, 'dashboard/profile_dashboard_section.html', {})


def get_proffesionals(request):
    print(request)
    '''
    Funcion que retorna todos los Profesionales de la base de datos.
    :param request:
    :return: Queryset Professionals
    '''

    try:
        p = Professional.objects.all()
        print(p)
        return render(
            request,
            'dashboard/profile/profile_professionals_section.html',
            {'professionals': p}
        )

    except Professional.DoesNotExist:
        print('Exception')
        return render(
            request,
            'dashboard/profile_dashboard_section.html'
        )

def get_one_proffesional(request, id):
    try:

        professional_data = Professional.objects.get(id=int(id))
        print(professional_data)
        return render(
            request,
            'dashboard/profile/profile_professionals_edit.html',
            {'professional': professional_data }

        )
    except Professional.DoesNotExist:
        return render(
            request,
            'dashboard/profile_dashboard_section.html'
        )