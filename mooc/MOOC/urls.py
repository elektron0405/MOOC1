from django.conf.urls import patterns, url
from MOOC import views

urlpatterns=patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^login.html$', views.login, name='login'),
	url(r'^loggedin.html$', views.loggedin, name='logged'),
	url(r'^register.html$', views.register, name='register'),
	url(r'^registered.html$', views.registered, name='registered'),
	url(r'^loadVid.html$', views.loadVideo, name='loadVideo'),
	url(r'^logout$', views.logout, name='logout')
)
