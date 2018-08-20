from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='profile'),
    url(r'^get_proffesionals/$', views.get_proffesionals, name='get_proffesionals')
]
