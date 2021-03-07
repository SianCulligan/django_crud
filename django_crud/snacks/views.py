from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model = Snack
    # this will create a form with 3 fields
    fields = ['name', 'description', 'owner']


class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model = Snack
    # this will create a form with 3 fields
    fields = ['name', 'description', 'owner']

class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')
