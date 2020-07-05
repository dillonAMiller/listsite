from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Checklist, item, pop, sets
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.
'''
def index(request):
    store_list = Checklist.objects.order_by('store_name')
    output = ', '.join([q.store_name for q in store_list])
    return HttpResponse(output)
'''
def index(request):
    store_list = Checklist.objects.order_by('store_name')
    template = loader.get_template('list/index.html')
    context = {
        'store_list': store_list,
    }
    return HttpResponse(template.render(context, request))

