from django.shortcuts import render,redirect


def index(request):
    return render(request, 'dashboard/profile_dashboard_section.html', {})
    #return redirect('/profile')
