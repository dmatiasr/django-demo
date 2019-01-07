from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
import json
from .session_functions import get_property_list_filter


def index(request):
    return render(request, 'main/rentapp_main_section.html', {})

def map_section(request):
    return render(request, 'main/map_section/map_section.html', {})

def redirect_property_list(request, parameter):
    return render(request, 'main/list_section/property_list_section.html', {'parameter': parameter})

def get_properties(request):
    properties = get_property_list_filter(request)
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(properties['properties'], 20)
        paginated_equipments = paginator.page(page)
    except EmptyPage:
        paginated_equipments = None
    context = {
        'property_list': paginated_equipments,
        'page': int(page),
        'numPages': paginator.num_pages
    }

    data = {
        'html': render_to_string('main/list_section/property_block_structure.html', context),
        'nextPage': paginator.page(page).next_page_number() if paginator.page(page).has_next() else 'null'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
