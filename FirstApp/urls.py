from django.urls import path
from . import views

urlpatterns = [path('', views.start_page, name = "Home"),
               path('posts/', views.posts.as_view(), name = "Posts-list"),
               path('posts/read-later', views.read_later, name = "Posts-to-be-read-later"),
               path('posts/<slug:slug>', views.post, name = "Post-details")]
