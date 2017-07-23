import random

from django.shortcuts import render


# function based view
def home(request):
    num = random.randint(0, 100000000)
    some_list = [num, random.randint(0, 100000000)]
    context = {
        'html_var': False,
        'num': num,
        'some_list': some_list
    }
    return render(request, "base.html", context)

