from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Item
from .forms import ItemForm


class ItemListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = "form.html"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        print(kwargs)
        return kwargs


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = "form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        print(kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Create Item'
        return context
