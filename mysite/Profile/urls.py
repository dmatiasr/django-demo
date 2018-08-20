from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='profile'),
    url(r'^get_proffesionals/$', views.get_proffesionals, name='get_proffesionals'),
    url(r'^professional/(?P<id>[0-9]+)$', views.get_one_proffesional, name='get_one_professional'),
]
