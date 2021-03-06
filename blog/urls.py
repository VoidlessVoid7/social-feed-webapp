from django.urls import path
from . import views
from .views import PostListView,PostCreateView


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('home1/',views.home1,name='blog-home1'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('analysis/',views.analysis,name='blog-analysis'),
    path('scrape/',views.scrape,name='blog-scrape'),
    path('nlp/',views.lp,name='blog-lp'),
]

