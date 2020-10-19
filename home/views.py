from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category
from .forms import PostForm
# Create your views here.
'''
def home_view(request, *args, **kwargs):
	#context = {'object': studentperformance.objects.all()}
	#return HttpResponse("<h1>Django 版本!<h1>")

	return render(request, "home/index.html", {})
'''

class Home_View(ListView):
	model = Post
	template_name = 'home/index.html'
	# ordering = ['-id']    					   # 讓最新的 post 在最上面
	ordering = ['-post_date']

class DetailPost_View(DetailView):
	model = Post
	template_name = 'post/detail_post.html'

class AddPost_View(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/add_post.html'
	# fields = '__all__'
	# fields = ('title', 'body')

class UpdatePost_View(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'post/update_post.html'
	#fields = ('title', 'title_tag', 'body')

class DeletePost_View(DeleteView):
	model = Post
	template_name = 'post/delete_post.html'
	success_url	= reverse_lazy('home')			# models.py 的 reverse 對 deletepost 無效

class AddCategory_View(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'post/add_category.html'
	fields = '__all__'


def Category_View(request, cats):
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'category/category.html', {'cats': cats.title(), 'category_posts': category_posts})