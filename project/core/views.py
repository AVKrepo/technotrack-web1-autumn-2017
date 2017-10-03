from django.shortcuts import render

# Create your views here.


def render_main_page(request):
    return render(request, "main_page.html")


def render_posts(request):
    return render(request, "posts.html")


def render_blogs(request):
    return render(request, "blogs.html")


def render_posts_in_blog(request, name):
    return render(request, "posts_in_blog.html", {'name': name})


def render_post(request, number):
    return render(request, "post.html", {'number': number})


def render_profile(request, name):
    return render(request, "profile.html", {'name': name})
