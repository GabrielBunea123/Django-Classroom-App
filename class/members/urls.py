from django.urls import path
from . import views as v
from django.contrib.auth import views as auth_views
from .views import UserRegisterView,UserEditView,PasswordsChangeView,EditProfilePageView,CreateProfilePageView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
]