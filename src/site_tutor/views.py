from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
import models



# list
def tutor_list(request):
    return object_list(request, models.Tutor.objects.all(), template_name="tutor_list.html") 

# create
def tutor_new(request):
	
	
    return create_object(request, model=models.Tutor, template_name="tutor_form.html");

# read
def tutor_view(request, id):
    return object_detail(request, models.Tutor.objects.all(), object_id = id, template_name="tuor_detail.html")
    
# update
def tutor_update(request, id):
    return update_object(request, model=models.Tutor ,object_id = id, template_name="tutor_update.html")
    
def tutor_delete(request, id):
    item=get_object_or_404(models.Tutor, id=id)
    item.delete()
    return HttpResponseRedirect(reverse('tutor_list'))
