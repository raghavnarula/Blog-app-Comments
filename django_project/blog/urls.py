from . import views
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,CommentCreateView

urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    # path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    path('post/<int:pk>', views.post_detail_view, name='post-detail'),
]