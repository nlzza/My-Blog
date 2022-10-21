from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def start_page(request):

    all_posts = Post.objects.all().order_by("-date")
    if request.method == "POST":
        read_later_list = request.session.get("read_later_list")
        if read_later_list is None:
            read_later_list = []
        post_id = int(request.POST['later'])
        if post_id not in read_later_list:
            read_later_list.append(post_id)
        request.session["read_later_list"] = read_later_list
    return render(request, "FirstApp/start_page.html", {"recent_posts": all_posts[:3]})

def read_later(request):
    
    read_later_list = request.session.get("read_later_list")
    posts = Post.objects.filter(id__in = read_later_list)
    return render(request, "FirstApp/all-posts.html", {"all_posts": posts,
                                                       "heading": "Posts marked as Read Later"})

class posts(ListView):

    template_name = "FirstApp/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "All Posts"
        return context

def post(request, slug):

    p = get_object_or_404(Post, slug = slug)
    form = None
    if request.method == "GET":
        form = CommentForm()
        read_later_list = request.session.get("read_later_list")
        if p.id in read_later_list:
            read_later_list.remove(p.id)
        request.session["read_later_list"] = read_later_list
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = p
            comment.save()
            form = CommentForm()
    comments = p.Comment.all()
    count = comments.count()
    return render(request, "FirstApp/post-details.html", {"post": p, "tags": p.tags.all(),
                                                          "comments": comments, "form": form,
                                                          "count": count})
