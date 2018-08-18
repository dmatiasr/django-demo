from django.shortcuts import render,redirect


def index(request):
    return redirect('/profile')

def profile(request):
    return render(request, 'dashboard/profile_dashboard_section.html', {})