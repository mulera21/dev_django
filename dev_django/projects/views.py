from django.shortcuts import render

# Create your views here.


def project(request):
    context ={}
    return  render(request, "project.html", context)

