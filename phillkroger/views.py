from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.utils import timezone

def mainapp(request):
    projects = Project.objects.all().order_by("-pubdate")
    return render(request, "mainapp/index.html", {"projects": projects})

class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
"""
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
"""

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    model = Post
    paginate_by = 100  # if pagination is desired


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return Post.objects.all()


def resume(request):

    return render(request, "mainapp/resume.html")

