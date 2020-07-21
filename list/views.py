from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Checklist, Set, Item, Pop
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import itemDisplayedForm, popDisplayedForm
from .models import itemIsDisplayedForm, popIsDisplayedForm

# from .forms import is_displayed_form


# Create your views here.
#useless index view
'''
def index(request):
    return HttpResponse("Checklist index")
'''
# view list of stores no template
'''
def index(request):
    store_list = Checklist.objects.order_by('store_name')
    output = ', '.join([q.store_name for q in store_list])
    return HttpResponse(output)
'''

# view with template
'''
def index(request):
    store_list = Checklist.objects.order_by('store_name')
    template = loader.get_template('list/index.html')
    context = {
        'store_list': store_list,
    }
    return HttpResponse(template.render(context, request))
'''

# view with template and render

def index(request):
    store_list = Checklist.objects.order_by('pub_date')
    context = {'store_list': store_list}
    return render(request, 'list/index.html', context)


def listIndex(request, Checklist_id):
    sets = get_list_or_404(Set)
    checklist = get_object_or_404(Checklist, pk=Checklist_id)
    set_list = Set.objects.order_by('id')
    context = {
        'checklist': checklist, 
        'set_list': set_list,
        'sets': sets
    }
    return render(request, 'list/listIndex.html', context)


# detail view without details
'''
def detail(request, Checklist_id):
    return HttpResponse("You're looking at checklist %s." % Checklist_id)
'''
# detail with Http404
'''
def detail(request, Checklist_id):
    try:
        checklist = Checklist.objects.get(pk=Checklist_id)
    except Checklist.DoesNotExist:
        raise Http404("Checklist does not exist")
    return render(request, 'list/detail.html', {'Checklist': Checklist})
'''
# detail with get_object_or_404
'''
def detail(request, Checklist_id):
    checklist = get_object_or_404(Checklist, pk=Checklist_id)
    item = Item.objects.get(pk=1)

    form = itemIsDisplayedForm(instance=item)
    
    form.save()
    return render(request, 'list/detail.html', {'checklist': checklist, 'form': form})

        
    
    # form = itemDisplayedForm(request.POST)
    
    # return render(request, 'list/detail.html', {'checklist': checklist, 'form': form})
'''

# detail with set list links
'''
def detail(request, Checklist_id, Set_id):
    set_list = Set.objects.order_by('set_name')
    context = {'set_list': set_list}
    sets = get_object_or_404(Set, pk=Set_id)
    checklist = get_object_or_404(Checklist, pk=Checklist_id)
    return render(request, 'list/detail.html', {'checklist': checklist}, {'sets': sets}, context)
'''


# is displayed form 


def setDetail(request, Checklist_id, Set_id):
    sets = get_object_or_404(Set, pk=Set_id)
    return render(request, 'list/setDetail.html', { 'sets': sets })

'''
class IndexView(generic.ListView):
    template_name = 'list.index.html'
    context_object_name = 'store_list'

    def get_queryset(self):
        return Checklist.objects.order_by('store_name')

class DetailView(generic.DetailView):
    model = Checklist
    template_name = 'list/detail.html'

    def get_queryset(self):
        return Checklist.objects
'''
 
