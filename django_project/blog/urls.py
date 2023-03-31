from django.urls import path
from .views import PostListView, PostDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CustomForm, CommentDelete

urlpatterns = [
    path("form/", CustomForm, name="custom_form"),

    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/com_delete/", CommentDelete.as_view(), name="comment_delete"),
    path("", PostListView.as_view(), name="home"),
]
