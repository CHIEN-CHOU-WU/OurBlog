from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, EditProfilePageForm, ProfilePageForm
from home.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	# form_class = PasswordChangeForm
	success_url = reverse_lazy('password-success')

def password_success(request):
	return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	# 傳入 categories 到新增頁 讓 Navbar 的 categories 可以讀取
	def get_context_data(self, *args, **kwargs):
		cat_menu = Profile.objects.all()		   # 建造 queryset
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)    # super 繼承 Home_View class
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context["page_user"] = page_user
		return context

class EditProfilePageView(generic.UpdateView):
	model = Profile
	form_class = EditProfilePageForm
	template_name = 'registration/edit_profile_page.html'
	
	success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = "registration/create_user_profile_page.html"
	# fields = '__all__'

	def form_valid(self, form):						#  創立個人資料時，這個函數讓系統知道要對應到哪個使用者
		form.instance.user = self.request.user
		return super().form_valid(form)
