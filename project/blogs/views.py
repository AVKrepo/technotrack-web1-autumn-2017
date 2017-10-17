from django.shortcuts import render
from django.views.generic import DetailView, ListView
from blogs.models import Post, Category


class PostsDetail(ListView):
    template_name = 'blogs/posts_detail.html'
    model = Post


class PostDetail(DetailView):
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


class CategoriesDetail(ListView):
    template_name = 'blogs/categories_detail.html'
    model = Category


class CategoryDetail(DetailView):
    template_name = 'blogs/category_detail.html'
    context_object_name = 'category'
    queryset = Category.objects.all()
