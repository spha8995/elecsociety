from django.conf.urls.defaults import *
from views import tutor_list, tutor_new, tutor_view, tutor_update, tutor_delete

urlpatterns = patterns('',
url("^$", tutor_list, name="tutor_list"),
url("^new/$", tutor_new, name="tutor_new"),
url("^view/(?P<id>[0-9]+)$", tutor_view, name="tutor_view"),
url("^update/(?P<id>[0-9]+)$", tutor_update, name="tutor_update"),
url("^delete/(?P<id>[0-9]+)$", tutor_delete, name="tutor_delete"),
url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)
