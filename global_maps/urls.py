from django.conf.urls import url, include
from django.urls import path


from . import views

urlpatterns = [
  url(r'^$', views.global_maps_view, name='global'),

#  url(r'^', views.index, name='index'),
#  url(r'^1/', views.kakogo, name='kakogo'),


]
