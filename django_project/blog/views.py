from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import( ListView,
                    CreateView,
                    DetailView,
                    TemplateView,
                    DeleteView,
                    UpdateView)
# ListView
# DetailView
# TemplateView
# CreateView
# UpdateView



class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False

# def home(request) :
#     context = {
#         "posts":Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


def about(request) :
    return render(request, 'blog/about.html')







# posts = [
#     {'title':'Post 1',
#      'description':'This the content of the post.',
#      'author':'Shiva',
#      'date_posted': 'Jan 9,2002',
#      },
#          {'title':'Post 2',
#      'description':'This is the content of the post.',
#      'author':'Krishna',
#      'date_posted': 'Sept 23, 1992',
#      }
# ]
# # Create your views here.
# def home(request) :

#     context = {
#         "posts":posts
#     }
#     return render(request, 'blog/home.html', context)

# def about(request) :
#     return render(request, 'blog/about.html')
