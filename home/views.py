from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

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

    # 傳入 categories 到首頁 讓 Navbar 的 categories 可以讀取
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(Home_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu

        return context


class DetailPost_View(DetailView):
    model = Post
    template_name = 'post/detail_post.html'

    # 傳入 categories 到詳細資訊 讓 Navbar 的 categories 可以讀取
    # 傳入 全部 讚數
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(DetailPost_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu
        # 傳入讚數
        temp = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = temp.total_likes()
        # 看看 讚 有沒有被取消
        liked = False
        if temp.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


class AddPost_View(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

    # 傳入 categories 到新增頁 讓 Navbar 的 categories 可以讀取
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(AddPost_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu
        return context


class UpdatePost_View(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update_post.html'
    #fields = ('title', 'title_tag', 'body')

    # 傳入 categories 到修改頁 讓 Navbar 的 categories 可以讀取
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(UpdatePost_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu
        return context


class DeletePost_View(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')			# models.py 的 reverse 對 deletepost 無效

    # 傳入 categories 到刪除頁 讓 Navbar 的 categories 可以讀取
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(DeletePost_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu
        return context


class AddCategory_View(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'post/add_category.html'
    fields = '__all__'

    # 傳入 categories 到新增種類頁 讓 Navbar 的 categories 可以讀取
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()		   # 建造 queryset
        context = super(AddCategory_View, self).get_context_data(
            *args, **kwargs)    # super 繼承 Home_View class
        context["cat_menu"] = cat_menu
        return context


# 瀏覽種類頁面用
def Category_View(request, cats):
    # replace('-', ' ') 如果 category 中間有空格會被 '-' 取代
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    cat_type = Category.objects.values('name')
    cat_menu = []
    for cates in cat_type:
        cat_menu.append(cates['name'])
    

    return render(request, 'category/category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts, 'cat_menu': cat_menu})


def Like_View(request, pk):
    post = get_object_or_404(Post, id=request.POST.get(
        'post_id'))    # button 的 name = post_id
    # 收回 like
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        # now save that like to the table (also the user)
        liked = True
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))
