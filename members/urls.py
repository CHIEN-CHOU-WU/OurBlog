from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
	path('register/', views.UserRegisterView.as_view(), name='register'),
	path('edit_setting/', views.UserEditView.as_view(), name='edit-setting'),
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
	path('password/', views.PasswordsChangeView.as_view(template_name='registration/change_password.html')),
	path('password_success', views.password_success, name='password-success'),
	path('<int:pk>/profile', views.ShowProfilePageView.as_view(), name='show-profile'),
	path('<int:pk>/edit_profile_page', views.EditProfilePageView.as_view(), name='edit-profile'),
	path('create_profile/', views.CreateProfilePageView.as_view(), name="create-profile"),

]