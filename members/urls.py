from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
	path('register/', views.UserRegisterView.as_view(), name='register'),
	path('edit_profile/', views.UserEditView.as_view(), name='edit-profile'),
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
	path('password/', views.PasswordsChangeView.as_view(template_name='registration/change_password.html')),
	path('password_success', views.password_success, name='password-success')

]