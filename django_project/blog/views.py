from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class MainView(TemplateView):
	template_name = 'blog/main_page.html'

class HomeView(TemplateView):
	template_name = 'blog/main_page.html'

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
