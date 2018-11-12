from django.conf.urls import url, include
from django.urls import path


from . import views

urlpatterns = [
  path('1/', views.kakogo),

#  url(r'^', views.index, name='index'),
#  url(r'^1/', views.kakogo, name='kakogo'),


]
