from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


class PostCreateView(CreateView):
    form_class = forms.PostForm
    model = models.Post


class PostUpdateView(UpdateView):
    form_class = forms.PostForm
    model = models.Post
    context_object_name = 'app'
    template_name = 'app/post_form.html'


class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = models.Post
