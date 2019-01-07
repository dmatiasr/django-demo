from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map_section/$', views.map_section, name='map_section'),
    url(r'^get_properties/$', views.get_properties, name='get_properties'),
    url(r'^list_section/list/(?P<parameter>[\w\-]+)/$', views.redirect_property_list, name='redirect_to_property_list'),
]