from django.conf.urls import url
from comments.views import CommentsDetail, CommentDetail


urlpatterns = [
    url(r'^$', CommentsDetail.as_view(), name='comments_detail'),
    url(r"^(?P<pk>\d+)/$", CommentDetail.as_view(), name='comment_detail'),
]