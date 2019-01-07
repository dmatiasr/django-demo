from .models import Property


def get_property_list_filter(request):
    activity = {'properties': []}
    property_filters = {}
    if 'parameter' in request.POST:
        if request.POST['parameter'] != 'all':
            property_filters['type'] = request.POST['parameter']