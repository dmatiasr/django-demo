from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/rentapp_main_section.html', {})

def map_section(request):
    return render(request, 'main/map_section/map_section.html', {})