import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    )

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return RestaurantLocation.objects.filter(
            owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        return RestaurantLocation.objects.filter(
            owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "form.html"
    # success_url = "/restaurants/"
    #login_url = "/login/"

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.owner = self.request.user
            return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/detail-update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Edit Restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(
            owner=self.request.user)