from django.urls import path

from . import views
urlpatterns = [
	path('', views.Home_View.as_view(), name="home"),
	path('details/<int:pk>', views.DetailPost_View.as_view(), name="post-details"),   # pk = primarykey
	path('add_post/', views.AddPost_View.as_view(), name="post-add"),
	path('details/edit/<int:pk>', views.UpdatePost_View.as_view(), name="post-edit"),
	path('details/<int:pk>/delete', views.DeletePost_View.as_view(), name="post-delete"),
	path('add_category/', views.AddCategory_View.as_view(), name="category-add"),
	
]