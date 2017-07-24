import random

from django.shortcuts import render
from django.views import View


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
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html", {})

    # def post(self, request, *args, **kwargs):
    #     return render(request, "contact.html", {})

    # def put(self, request, *args, **kwargs):
    #     return render(request, "contact.html", {})
