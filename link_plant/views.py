from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    # Template called model_list.html -> link_list.html

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # Template called model_form.html -> link_form.html

class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    # Template called model_form.html -> link_form.html

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    # Template called model_confirm_delete.html -> link_confirm_delete.html