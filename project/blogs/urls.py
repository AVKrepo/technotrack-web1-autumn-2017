from django.conf.urls import url
from blogs.views import *


urlpatterns = [
    url(r'^posts/$', PostsDetail.as_view(), name='posts_detail'),
    url(r"^posts/(?P<pk>\d+)/$", PostDetail.as_view(), name='post_detail'),
    url(r'^categories/$', CategoriesDetail.as_view(), name='categories_detail'),
    url(r"^categories/(?P<pk>\d+)/$", CategoryDetail.as_view(), name='category_detail'),

]