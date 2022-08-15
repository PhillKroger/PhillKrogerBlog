from django.shortcuts import render
from .models import *


def mainapp(request):
    projects = Project.objects.all().order_by("-pubdate")
    return render(request, "base.html", {"projects": projects})

