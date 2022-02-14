from django import urls
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django. shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    # Este mixin requerira que el usuario sea miembro del staff
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self).dispatch(request, *args, **kwargs)

# Create your views here.

class PageListView(ListView):           # ListView
    model = Page                     

class PageDetailsView(DetailView):      # DetailsView
    model = Page                    

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):       # CreateView
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):       # UpdateView
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:pages') #, args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):       # DeleteView
    model = Page
    success_url = reverse_lazy('pages:pages')