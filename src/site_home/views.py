from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
import models

# list
def example_food_list(request):
    return object_list(request, models.Food.objects.all(), template_name="food_list.html") 

# create
def example_food_new(request):
    return create_object(request, model=models.Food, template_name="food_form.html");

# read
def example_food_view(request, id):
    return object_detail(request, models.Food.objects.all(), object_id = id, template_name="food_detail.html")
    
# update
def example_food_update(request, id):
    return update_object(request, model=models.Food ,object_id = id, template_name="food_update.html")
    
def example_food_delete(request, id):
    item=get_object_or_404(models.Food, id=id)
    item.delete()
    return HttpResponseRedirect(reverse('food_list'))