from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^forum/', include("site_forum.urls")),
	url(r'^money/', include("site_money.urls")),
	url(r'^tutor/', include("site_tutor.urls")),
	url(r'^', include("site_home.urls")),
)
