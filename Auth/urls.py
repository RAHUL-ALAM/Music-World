from django.conf.urls import url, include
from django.contrib.auth.views import logout
from . import views 

urlpatterns = [
	url(r'^$',views.home),
	url(r'^LoginRegister/',views.logreg),
	url(r'^login/',views.Login),
	url(r'register/',views.Register),
	url(r'^logout/$', logout, {'next_page': '/'}),
]