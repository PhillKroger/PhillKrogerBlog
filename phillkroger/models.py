from django.db import models
from django.db.models import TextField


class Tag(models.Model):
    tag_name = models.CharField("Tag Name", max_length=255, unique=True, blank=True, default='Tag')

    def __str__(self):
        return self.tag_name

class ProjectCategory(models.Model):
    category_name = models.CharField("Project Category Name", max_length=128, unique=True, blank=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    title = models.CharField("Project Title", max_length=255)
    description = models.TextField("Description", max_length=10000, default="PhillKroger's Project")
    tags = models.ManyToManyField(Tag)
    project_preview = models.ImageField("Project Preview")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    link = models.URLField("Project Link", max_length=128, unique=True, blank=True, default=None)
    project_github = models.URLField("Project Github", max_length=128, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"