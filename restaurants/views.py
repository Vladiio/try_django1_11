import random

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# function based view
def home(request):
    num = random.randint(0, 100000000)
    some_list = [num, random.randint(0, 100000000)]
    context = {
        'html_var': True,
        'num': num,
        'some_list': some_list
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


# class-based views
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        num = random.randint(0, 100000000)
        some_list = [num, random.randint(0, 100000000)]
        data = {
            'html_var': True,
            'num': num,
            'some_list': some_list
        }
        context.update(data)
        print(context)
        return context
