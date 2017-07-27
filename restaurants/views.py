import random

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_create_view(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/restaurants/')
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, "restaurants/form.html", context)


def restaurant_list_view(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                        Q(category__iexact=slug) |
                        Q(category__icontains=slug))
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/form.html"
    success_url = "/restaurants/"
