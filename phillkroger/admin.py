from django.contrib import admin
from .models import ProjectCategory, Tag, Project

admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(Tag)