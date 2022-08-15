from django.urls import path
from . import views
from .views import PostDetailView, PostListView

urlpatterns = [
    path('', views.mainapp, name="mainapp"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('resume/', views.resume, name="resume"),
]