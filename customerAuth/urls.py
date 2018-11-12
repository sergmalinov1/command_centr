from django.conf.urls import url, include
from customerAuth import views

urlpatterns = [

  url(r'^signup/$', views.signup, name='signup'),

  url(r'^login/$', views.login, name='login'),
 # url(r'^login/verifications/$', views.loginVerifications, name='index'),



]
