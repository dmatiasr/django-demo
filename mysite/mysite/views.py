from django.shortcuts import render, redirect


def index(request):
    """
    View function for index page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'mysite_base.html',
    )
