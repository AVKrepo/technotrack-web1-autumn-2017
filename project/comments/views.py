from django.shortcuts import render
from django.views.generic import DetailView, ListView
from comments.models import Comment


class CommentsDetail(ListView):
    template_name = 'comments/comments_detail.html'
    model = Comment


class CommentDetail(DetailView):
    template_name = 'comments/comment_detail.html'
    context_object_name = 'comments'
    queryset = Comment.objects.all()
