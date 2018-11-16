from django.conf.urls import url, include
from account import views
from django.contrib.auth.views import LoginView

urlpatterns = [

  url(r'^login/$', LoginView.as_view(template_name='account/login.html')),
  url(r'^signup/$', views.signup, name='signup'),


 # url(r'^login/verifications/$', views.loginVerifications, name='index'),
#  url(r'^login/$', LoginView.as_view(template_name='account/login.html')),



]
