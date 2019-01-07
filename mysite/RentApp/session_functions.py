from .models import Property


def get_property_list_filter(request):
    activity = {'properties': []}
    property_filters = {}
    if 'type' in request.POST:
        if request.POST['type'] != 'all':
            property_filters['type'] = request.POST['type']

    print(property_filters)
    activity['properties'] = Property.objects.filter(**property_filters)
    return activity
