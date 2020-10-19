from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)    # CASCADE 刪除作者，會一起刪除
	body = models.TextField()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):                                   # CreateView 需要用到
		#return reverse('post-details', args=(str(self.id)))
		return reverse('home')               # 回主頁 home