"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
import core.views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    # url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    # url(r'^$', core.views.render_main_page),
    # url(r"^blogs/$", core.views.render_blogs),
    # url(r"^blogs/(?P<name>\w+)/$", core.views.render_posts_in_blog),
    # url(r"^posts/$", core.views.render_posts),
    # url(r"^posts/(?P<number>\d+)/$", core.views.render_post),
    # url(r"^user/(?P<name>\w*)/$", core.views.render_profile),
]

if settings.DEBUG is True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

