from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def project(request, pk):
    context = {}
    return render(request, "project.html", context)


