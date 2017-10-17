from django.shortcuts import render
from django.views.generic import DetailView, ListView
from core.models import User


class UsersDetail(ListView):
    template_name = 'core/users_detail.html'
    context_object_name = 'users'
    queryset = User.objects.all()


class UserDetail(DetailView):
    template_name = 'core/user_detail.html'
    model = User
    context_object_name = 'user'



# def render_profile(request, name):
#     return render(request, "profile.html", {'name': name})
