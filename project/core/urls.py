from django.conf.urls import url
from core.views import UserDetail, UsersDetail


urlpatterns = [
    url(r'^$', UsersDetail.as_view(), name='users_detail'),
    url(r"^(?P<pk>\d+)/$", UserDetail.as_view(), name='user_detail'),
]