from django.shortcuts import render
from .models import *


def mainapp(request):
    projects = Project.objects.all()  # .order_by()[-1::]
    return render(request, "base.html", {"projects": projects})


"""
def index(request):
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"people": people})

def sets(request):
    sets = Set.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sets, 20)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'products/filter_set.html', {'sets': sets})
"""
