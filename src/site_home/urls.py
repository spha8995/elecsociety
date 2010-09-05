from django.conf.urls.defaults import *
from views import example_food_list, example_food_new, example_food_view, example_food_update, example_food_delete

urlpatterns = patterns('',
url("^example/food/$", example_food_list, name="food_list"),
url("^example/food/new$", example_food_new, name="food_new"),
url("^example/food/view/(?P<id>[0-9]+)$", example_food_view, name="food_view"),
url("^example/food/update/(?P<id>[0-9]+)$", example_food_update, name="food_update"),
url("^example/food/delete/(?P<id>[0-9]+)$", example_food_delete, name="food_delete"),
url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)