from django.shortcuts import render


# function based view
def home(request):
    return render(request, "base.html", {})

