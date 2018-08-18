from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.index, name='profile'),
    #url(r'^profile$', views.profile, name='profile_dashboard')
]