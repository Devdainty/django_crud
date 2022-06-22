from django.views import generic
from .models import Post
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class  PostDetailView(generic.DetailView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class  PostDeleteView(generic.DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
