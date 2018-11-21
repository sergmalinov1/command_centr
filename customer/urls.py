from django.conf.urls import url, include
from customer import views
from django.contrib.auth.views import LoginView

urlpatterns = [

  url(r'^$', views.index, name='index'),
  url(r'^signup/$', views.signup_view, name='signup'),
  url(r'^login/$', LoginView.as_view(template_name='customer/login.html'), name='login'),
 # url(r'^login/$',  views.login_view,  name='login'),
  url(r'^logout/$', views.logout_view, name='logout'),

  url(r'^profile/$', views.profile_view, name='profile'),
  url(r'^password_reset/$', views.password_reset_view, name='password_reset'),

 # url(r'^login/verifications/$', views.loginVerifications, name='index'),




]
