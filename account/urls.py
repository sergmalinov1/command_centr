from django.conf.urls import url, include
from account import views
from django.contrib.auth.views import LoginView

urlpatterns = [

  url(r'^$', views.index, name='index'),
  url(r'^signup/$', views.signup_view, name='signup'),
  url(r'^login/$', LoginView.as_view(template_name='account/login.html')),
 # url(r'^login/$',  views.login_view,  name='login'),
  url(r'^logout/$', views.logout_view, name='logout'),


 # url(r'^login/verifications/$', views.loginVerifications, name='index'),




]
