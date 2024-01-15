from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="home-page"),
    path("posts", views.AllPostsView.as_view(), name="all-posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="single-post-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
]
